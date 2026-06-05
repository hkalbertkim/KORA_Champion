"""Schema helpers for routing benchmark workload records."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from kora_core.compat import StrEnum


class RoutePath(StrEnum):
    DETERMINISTIC = "deterministic"
    CACHE = "cache"
    CPU = "cpu"
    PROVIDER = "provider"
    LOCAL_GPU = "local_gpu"
    FALLBACK = "fallback"


def _validate_route_path(value: Any) -> None:
    try:
        RoutePath(str(value))
    except ValueError as exc:
        raise ValueError(f"unsupported oracle route: {value}") from exc


REQUIRED_PROFILES = {
    "mixed_realistic_100k",
    "gpu_heavy_100k",
    "cache_heavy_100k",
    "adversarial_100k",
    "service_replay_10k",
}


@dataclass(frozen=True)
class RouterVisibleMetadata:
    observable: dict[str, Any]
    inferred: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {"observable": dict(self.observable), "inferred": dict(self.inferred)}


@dataclass(frozen=True)
class OracleLabels:
    expected_route: str
    acceptable_routes: list[str]
    disallowed_routes: list[str]
    oracle_reason: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "expected_route": self.expected_route,
            "acceptable_routes": list(self.acceptable_routes),
            "disallowed_routes": list(self.disallowed_routes),
            "oracle_reason": self.oracle_reason,
        }


@dataclass(frozen=True)
class ComputeWeight:
    value: float
    method: str
    formula_version: str
    basis: dict[str, Any]
    measured_weight_available: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "value": self.value,
            "method": self.method,
            "formula_version": self.formula_version,
            "basis": dict(self.basis),
            "measured_weight_available": self.measured_weight_available,
        }


@dataclass(frozen=True)
class ValidationMetadata:
    quality_check_required: bool
    cache_hit_expected: bool
    adversarial_tag: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "quality_check_required": self.quality_check_required,
            "cache_hit_expected": self.cache_hit_expected,
            "adversarial_tag": self.adversarial_tag,
        }


@dataclass(frozen=True)
class BenchmarkRequest:
    request_id: str
    workload_profile: str
    workload_class: str
    router_visible_metadata: RouterVisibleMetadata
    oracle_labels: OracleLabels
    compute_weight: ComputeWeight
    validation: ValidationMetadata

    def router_input(self) -> dict[str, Any]:
        return {
            "request_id": self.request_id,
            "workload_profile": self.workload_profile,
            "workload_class": self.workload_class,
            "router_visible_metadata": self.router_visible_metadata.to_dict(),
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "request_id": self.request_id,
            "workload_profile": self.workload_profile,
            "workload_class": self.workload_class,
            "router_visible_metadata": self.router_visible_metadata.to_dict(),
            "oracle_labels": self.oracle_labels.to_dict(),
            "compute_weight": self.compute_weight.to_dict(),
            "validation": self.validation.to_dict(),
        }


def validate_request(record: Mapping[str, Any]) -> None:
    required = {
        "request_id",
        "workload_profile",
        "workload_class",
        "router_visible_metadata",
        "oracle_labels",
        "compute_weight",
        "validation",
    }
    missing = required.difference(record)
    if missing:
        raise ValueError(f"missing required request fields: {sorted(missing)}")
    if record["workload_profile"] not in REQUIRED_PROFILES:
        raise ValueError(f"unsupported workload profile: {record['workload_profile']}")
    metadata = record["router_visible_metadata"]
    if not isinstance(metadata, Mapping) or "observable" not in metadata or "inferred" not in metadata:
        raise ValueError("router_visible_metadata must include observable and inferred sections")
    labels = record["oracle_labels"]
    try:
        RoutePath(str(labels["expected_route"]))
    except ValueError as exc:
        raise ValueError(f"unsupported expected route: {labels['expected_route']}") from exc
    for route in labels["acceptable_routes"] + labels["disallowed_routes"]:
        _validate_route_path(route)
    if record["compute_weight"]["formula_version"] != "cw_v0_1":
        raise ValueError("compute weight formula_version must be cw_v0_1")


def workload_to_json_dict(requests: list[BenchmarkRequest]) -> dict[str, Any]:
    return {
        "schema_version": "routing_benchmark_workload_v0_1",
        "request_count": len(requests),
        "requests": [request.to_dict() for request in requests],
    }


def requests_from_json_dict(payload: Mapping[str, Any]) -> list[dict[str, Any]]:
    if payload.get("schema_version") != "routing_benchmark_workload_v0_1":
        raise ValueError("unsupported workload schema_version")
    requests = list(payload.get("requests", []))
    for request in requests:
        validate_request(request)
    return requests
