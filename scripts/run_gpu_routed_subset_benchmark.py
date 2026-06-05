#!/usr/bin/env python3
"""Run the routed GPU subset measurement with sanitized evidence output."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib
import json
import math
import shutil
import subprocess
import sys
import threading
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from io import StringIO
from pathlib import Path
from typing import Any, Iterable, Mapping

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
SCRIPT_DIR = REPO_ROOT / "scripts"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from kora_core.routing_benchmark.kora_router_adapter import kora_router_adapter  # noqa: E402
from kora_core.routing_benchmark.routers import ROUTER_POLICIES, router_input_from_request  # noqa: E402
from kora_core.routing_benchmark.workload_generator import generate_workload  # noqa: E402
from run_gpu_smoke_workload import collect_gpu_snapshot  # noqa: E402

TASK_ID = "KORA-CHAMPION-GPU-004C"
DEFAULT_OUTPUT_DIR = Path("docs/evidence/gpu-routed-subset-runs")
ROUTER_FUNCTIONS = {**ROUTER_POLICIES, "kora_router_adapter": kora_router_adapter}
CLASS_DIMENSIONS = {
    "embedding_index_query_large": 192,
    "embedding_similarity": 160,
    "gpu_batch_embedding": 224,
    "gpu_tensor_transform": 256,
    "image_like_compute": 288,
    "rerank_batch_large": 192,
    "batch_tensor_operation": 256,
}
MAX_DIMENSION = 320


def main() -> int:
    args = _parse_args()
    evidence = run_routed_subset_benchmark(
        comparison_run=args.comparison_run,
        router=args.router,
        limit=args.limit,
        output_dir=args.output_dir,
        local_validation_only=args.local_validation_only,
        sampling_interval_seconds=args.sampling_interval_seconds,
    )
    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = (
        evidence["timestamp_utc"]
        .replace("-", "")
        .replace(":", "")
        .replace(".", "")
        .replace("+00:00", "Z")
        .replace("+0000", "Z")
        .replace("T", "-")
    )
    evidence_path = output_dir / f"{timestamp}-mixed_realistic_100k-kora-router-h100-subset.json"
    evidence_path.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "evidence_path": str(evidence_path),
                "claim_level": evidence["claim_level"],
                "cuda_available": evidence["gpu_runtime"]["cuda_available"],
                "h100_execution": evidence["h100_execution"],
                "measured_subset_count": evidence["measured_subset"]["measured_subset_count"],
                "runtime_seconds": evidence["gpu_runtime"]["runtime_seconds"],
                "throughput_requests_per_second": evidence["gpu_runtime"]["throughput_requests_per_second"],
                "error_count": evidence["gpu_runtime"]["error_count"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    if not args.local_validation_only and not evidence["gpu_runtime"]["cuda_available"]:
        return 2
    return 0


def run_routed_subset_benchmark(
    *,
    comparison_run: Path,
    router: str,
    limit: int,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    local_validation_only: bool = False,
    sampling_interval_seconds: float = 0.2,
) -> dict[str, Any]:
    if limit <= 0:
        raise ValueError("limit must be positive")
    comparison = json.loads(comparison_run.read_text(encoding="utf-8"))
    source_summary_run = str(comparison_run.with_name(f"{comparison_run.stem}-summary.json"))
    if router not in ROUTER_FUNCTIONS:
        raise ValueError(f"unsupported router: {router}")

    profile = str(comparison["profile"])
    seed = int(comparison["seed"])
    total_requests = int(comparison["workload_request_count"])
    router_metrics = comparison["router_results"][router]
    workload = generate_workload(profile, total_requests, seed=seed)
    gpu_routed = select_gpu_routed_requests([request.to_dict() for request in workload], router)
    if len(gpu_routed) != int(router_metrics["route_counts"]["local_gpu"]):
        raise ValueError("reconstructed local_gpu count does not match source comparison")
    selected_subset = gpu_routed[: min(limit, len(gpu_routed))]
    measured_subset_compute_weight = round(sum(float(request["compute_weight"]["value"]) for request in selected_subset), 6)
    selection_hash = subset_selection_hash(selected_subset, router=router, limit=limit)
    runtime = execute_gpu_subset(
        selected_subset,
        local_validation_only=local_validation_only,
        sampling_interval_seconds=sampling_interval_seconds,
    )
    h100_execution = bool(runtime["cuda_available"] and not local_validation_only)
    claim_level = "gpu_routed_subset_measured" if h100_execution else "gpu_routed_subset_not_measured"
    if local_validation_only:
        claim_level = "local_validation_only"
    all_gpu_baseline_compute_weight = float(router_metrics["baseline_gpu_compute_weight"])
    kora_local_gpu_compute_weight = float(router_metrics["router_gpu_compute_weight"])
    estimated_all_gpu_runtime_seconds = estimate_all_gpu_runtime_seconds(
        measured_runtime_seconds=runtime["runtime_seconds"],
        measured_subset_compute_weight=measured_subset_compute_weight,
        all_gpu_baseline_compute_weight=all_gpu_baseline_compute_weight,
    )
    estimated_kora_full_subset_runtime_seconds = estimate_all_gpu_runtime_seconds(
        measured_runtime_seconds=runtime["runtime_seconds"],
        measured_subset_compute_weight=measured_subset_compute_weight,
        all_gpu_baseline_compute_weight=kora_local_gpu_compute_weight,
    )
    estimated_avoided = max(0.0, estimated_all_gpu_runtime_seconds - estimated_kora_full_subset_runtime_seconds)
    reduction = 0.0
    if estimated_all_gpu_runtime_seconds > 0:
        reduction = estimated_avoided / estimated_all_gpu_runtime_seconds

    timestamp = datetime.now(timezone.utc).isoformat()
    run_id = f"gpu004c-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}-{selection_hash[:12]}"
    return {
        "run_metadata": {
            "run_id": run_id,
            "timestamp_utc": timestamp,
            "task_id": TASK_ID,
            "profile": profile,
            "source_comparison_run": str(comparison_run),
            "source_summary_run": source_summary_run,
            "router": router,
            "claim_level": claim_level,
            "h100_execution": h100_execution,
            "live_provider_execution": False,
        },
        "run_id": run_id,
        "timestamp_utc": timestamp,
        "task_id": TASK_ID,
        "profile": profile,
        "source_comparison_run": str(comparison_run),
        "source_summary_run": source_summary_run,
        "router": router,
        "claim_level": claim_level,
        "h100_execution": h100_execution,
        "live_provider_execution": False,
        "routing_source_metrics": {
            "total_requests": total_requests,
            "kora_local_gpu_routed_count": len(gpu_routed),
            "kora_local_gpu_routed_percentage": round((len(gpu_routed) / total_requests) * 100.0, 6),
            "kora_local_gpu_compute_weight": kora_local_gpu_compute_weight,
            "all_gpu_baseline_compute_weight": all_gpu_baseline_compute_weight,
            "compute_weighted_gpu_reduction_percentage_vs_all_gpu": router_metrics[
                "compute_weighted_gpu_reduction_percentage"
            ],
            "exact_route_accuracy": router_metrics["exact_route_accuracy"],
            "acceptable_route_rate": router_metrics["acceptable_route_rate"],
            "unsafe_misroute_rate": router_metrics["unsafe_misroute_rate"],
            "fallback_rate": router_metrics["fallback_rate"],
        },
        "measured_subset": {
            "measured_subset_count": len(selected_subset),
            "measured_subset_compute_weight": measured_subset_compute_weight,
            "measured_subset_selection_method": "deterministic_first_n_local_gpu_routes",
            "measured_subset_limit": limit,
            "measured_subset_sha256": selection_hash,
        },
        "gpu_runtime": runtime,
        "baseline_comparison": {
            "estimated_all_gpu_runtime_seconds": round(estimated_all_gpu_runtime_seconds, 6),
            "measured_kora_subset_runtime_seconds": runtime["runtime_seconds"],
            "estimated_kora_full_gpu_subset_runtime_seconds": round(estimated_kora_full_subset_runtime_seconds, 6),
            "estimated_avoided_gpu_runtime_seconds": round(estimated_avoided, 6),
            "estimated_runtime_reduction_percentage": round(reduction * 100.0, 6),
            "baseline_method": "compute_weight_scaled_from_measured_routed_subset",
            "baseline_limitations": [
                "All-GPU baseline runtime is estimated from compute weight, not fully measured.",
                "Synthetic GPU operations approximate benchmark classes and are not model inference.",
            ],
        },
        "claim_boundary": {
            "measured_h100_routed_subset": h100_execution,
            "production_cost_savings_claim": False,
            "customer_workload_claim": False,
            "full_production_representativeness_claim": False,
            "provider_cost_claim": False,
        },
    }


def select_gpu_routed_requests(requests: list[Mapping[str, Any]], router: str) -> list[dict[str, Any]]:
    route_fn = ROUTER_FUNCTIONS[router]
    selected: list[dict[str, Any]] = []
    for request in requests:
        decision = route_fn(router_input_from_request(request))
        if decision.route == "local_gpu":
            selected.append(dict(request))
    return selected


def subset_selection_hash(requests: Iterable[Mapping[str, Any]], *, router: str, limit: int) -> str:
    digest = hashlib.sha256()
    digest.update(f"{router}:{limit}".encode("utf-8"))
    for request in requests:
        digest.update(str(request["request_id"]).encode("utf-8"))
        digest.update(str(request["workload_class"]).encode("utf-8"))
        digest.update(str(request["compute_weight"]["value"]).encode("utf-8"))
    return digest.hexdigest()


def operation_dimension(request: Mapping[str, Any]) -> int:
    workload_class = str(request["workload_class"])
    observable = request["router_visible_metadata"]["observable"]
    compute_weight = float(request["compute_weight"]["value"])
    input_size = int(observable["input_size"])
    batch_size = int(observable["batch_size"])
    base = CLASS_DIMENSIONS.get(workload_class, 160)
    size_component = int(math.log2(max(2, input_size)) * 8)
    batch_component = min(64, int(math.log2(max(2, batch_size + 1)) * 10))
    weight_component = min(64, int(math.sqrt(max(1.0, compute_weight))))
    return max(64, min(MAX_DIMENSION, base + size_component + batch_component + weight_component))


def execute_gpu_subset(
    requests: list[Mapping[str, Any]],
    *,
    local_validation_only: bool,
    sampling_interval_seconds: float,
) -> dict[str, Any]:
    torch_module = _load_torch()
    torch_available = torch_module is not None
    cuda_available = bool(torch_available and torch_module.cuda.is_available() and not local_validation_only)
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    if not cuda_available:
        return _empty_runtime(
            requests=requests,
            torch_available=torch_available,
            torch_version=str(getattr(torch_module, "__version__", None)) if torch_available else None,
            python_version=python_version,
            cuda_available=False,
            sampling_interval_seconds=sampling_interval_seconds,
        )

    device_count = int(torch_module.cuda.device_count())
    gpu_models = [str(torch_module.cuda.get_device_name(index)) for index in range(device_count)]
    per_class_counts = Counter(str(request["workload_class"]) for request in requests)
    per_class_runtime: dict[str, float] = defaultdict(float)
    checksum = 0.0
    error_count = 0
    samples: list[dict[str, Any]] = []
    sampler = SnapshotSampler(samples=samples, interval_seconds=sampling_interval_seconds)
    sampler.start()
    start = time.monotonic()
    try:
        for index, request in enumerate(requests):
            device = torch_module.device(f"cuda:{index % max(1, device_count)}")
            class_start = time.monotonic()
            try:
                checksum += run_request_operation(torch_module, request, device)
            except Exception:
                error_count += 1
                break
            finally:
                per_class_runtime[str(request["workload_class"])] += time.monotonic() - class_start
        if requests:
            torch_module.cuda.synchronize()
    finally:
        runtime_seconds = round(time.monotonic() - start, 6)
        sampler.stop()
    runtime_compute_weight = sum(float(request["compute_weight"]["value"]) for request in requests[: len(requests) - error_count])
    output_digest = hashlib.sha256(f"{checksum:.8f}:{len(requests)}:{error_count}".encode("utf-8")).hexdigest()
    utilization = summarize_samples(samples, "utilization_gpu_percent")
    memory = summarize_samples(samples, "memory_used_mb")
    memory_total = max(
        (
            float(gpu["memory_total_mb"])
            for sample in samples
            for gpu in sample.get("gpus", [])
            if gpu.get("memory_total_mb") is not None
        ),
        default=None,
    )
    return {
        "cuda_available": True,
        "torch_available": torch_available,
        "gpu_count": device_count,
        "gpu_models": sorted(set(gpu_models)),
        "torch_version": str(torch_module.__version__),
        "python_version": python_version,
        "runtime_seconds": runtime_seconds,
        "throughput_requests_per_second": _rate(len(requests) - error_count, runtime_seconds),
        "throughput_compute_weight_per_second": _rate(runtime_compute_weight, runtime_seconds),
        "per_class_counts": dict(sorted(per_class_counts.items())),
        "per_class_runtime_seconds": {key: round(value, 6) for key, value in sorted(per_class_runtime.items())},
        "checksum": round(checksum, 8),
        "output_digest": output_digest,
        "error_count": error_count,
        "error_rate": round(error_count / len(requests), 6) if requests else 0.0,
        "gpu_utilization_avg": utilization["average"],
        "gpu_utilization_max": utilization["max"],
        "gpu_memory_mb_avg": memory["average"],
        "gpu_memory_mb_max": memory["max"],
        "gpu_memory_total_mb": memory_total,
        "sampling_method": "nvidia-smi",
        "sampling_interval_seconds": sampling_interval_seconds,
    }


def run_request_operation(torch_module: Any, request: Mapping[str, Any], device: Any) -> float:
    dimension = operation_dimension(request)
    seed = int(hashlib.sha256(str(request["request_id"]).encode("utf-8")).hexdigest()[:8], 16)
    generator = torch_module.Generator(device=device)
    generator.manual_seed(seed)
    left = torch_module.randn((dimension, dimension), generator=generator, device=device, dtype=torch_module.float32)
    right = torch_module.randn((dimension, dimension), generator=generator, device=device, dtype=torch_module.float32)
    product = left @ right
    transformed = torch_module.nn.functional.normalize(torch_module.sin(product) + torch_module.cos(product), dim=1)
    reduced = transformed.sum()
    return float(reduced.detach().cpu().item())


def _empty_runtime(
    *,
    requests: list[Mapping[str, Any]],
    torch_available: bool,
    torch_version: str | None,
    python_version: str,
    cuda_available: bool,
    sampling_interval_seconds: float,
) -> dict[str, Any]:
    return {
        "cuda_available": cuda_available,
        "torch_available": torch_available,
        "gpu_count": 0,
        "gpu_models": [],
        "torch_version": torch_version,
        "python_version": python_version,
        "runtime_seconds": 0.0,
        "throughput_requests_per_second": None,
        "throughput_compute_weight_per_second": None,
        "per_class_counts": dict(sorted(Counter(str(request["workload_class"]) for request in requests).items())),
        "per_class_runtime_seconds": {},
        "checksum": None,
        "output_digest": subset_selection_hash(requests, router="local_validation_only", limit=len(requests)),
        "error_count": 0,
        "error_rate": 0.0,
        "gpu_utilization_avg": None,
        "gpu_utilization_max": None,
        "gpu_memory_mb_avg": None,
        "gpu_memory_mb_max": None,
        "gpu_memory_total_mb": None,
        "sampling_method": "not_available",
        "sampling_interval_seconds": sampling_interval_seconds,
    }


class SnapshotSampler:
    def __init__(self, *, samples: list[dict[str, Any]], interval_seconds: float) -> None:
        self.samples = samples
        self.interval_seconds = interval_seconds
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)

    def start(self) -> None:
        self._thread.start()

    def stop(self) -> None:
        self._stop.set()
        self._thread.join(timeout=max(1.0, self.interval_seconds * 4))

    def _run(self) -> None:
        while not self._stop.is_set():
            self.samples.append(collect_gpu_snapshot())
            self._stop.wait(self.interval_seconds)
        self.samples.append(collect_gpu_snapshot())


def summarize_samples(samples: list[Mapping[str, Any]], key: str) -> dict[str, float | None]:
    values = [
        float(gpu[key])
        for sample in samples
        for gpu in sample.get("gpus", [])
        if gpu.get(key) is not None
    ]
    if not values:
        return {"average": None, "max": None}
    return {"average": round(sum(values) / len(values), 6), "max": round(max(values), 6)}


def estimate_all_gpu_runtime_seconds(
    *,
    measured_runtime_seconds: float,
    measured_subset_compute_weight: float,
    all_gpu_baseline_compute_weight: float,
) -> float:
    if measured_runtime_seconds <= 0 or measured_subset_compute_weight <= 0:
        return 0.0
    return measured_runtime_seconds * (all_gpu_baseline_compute_weight / measured_subset_compute_weight)


def _rate(value: float, runtime_seconds: float) -> float | None:
    if runtime_seconds <= 0:
        return None
    return round(value / runtime_seconds, 6)


def _load_torch() -> Any | None:
    try:
        return importlib.import_module("torch")
    except Exception:
        return None


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the routed GPU subset benchmark.")
    parser.add_argument("--comparison-run", type=Path, required=True)
    parser.add_argument("--router", default="kora_router_adapter", choices=sorted(ROUTER_FUNCTIONS))
    parser.add_argument("--limit", type=int, default=10_000)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--local-validation-only", action="store_true")
    parser.add_argument("--sampling-interval-seconds", type=float, default=0.2)
    return parser.parse_args()


if __name__ == "__main__":
    raise SystemExit(main())
