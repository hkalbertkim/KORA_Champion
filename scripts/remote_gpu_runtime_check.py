#!/usr/bin/env python3
"""Print public-safe commands for checking a GPU Python runtime."""

from __future__ import annotations


CHECKS = [
    ("Python version", "python3 --version"),
    ("Pip availability", "python3 -m pip --version"),
    ("Venv availability", "python3 -m venv --help"),
    ("GPU snapshot", "nvidia-smi --query-gpu=name,index,driver_version --format=csv,noheader,nounits"),
    (
        "Torch CUDA check",
        "python3 - <<'PY'\n"
        "try:\n"
        "    import torch\n"
        "    print('torch_available=True')\n"
        "    print('torch_version=', torch.__version__)\n"
        "    print('cuda_available=', torch.cuda.is_available())\n"
        "    print('cuda_device_count=', torch.cuda.device_count())\n"
        "    if torch.cuda.is_available():\n"
        "        print('cuda_device_name_0=', torch.cuda.get_device_name(0))\n"
        "except Exception as exc:\n"
        "    print('torch_available=False')\n"
        "    print('torch_error_type=', type(exc).__name__)\n"
        "PY",
    ),
]

SETUP = [
    "python3 -m venv .venv",
    ". .venv/bin/activate",
    "python -m pip install --upgrade pip",
    "python -m pip install torch --index-url https://download.pytorch.org/whl/cu121",
]

SMOKE = [
    ".venv/bin/python run_gpu_smoke_workload.py --workload-size 100",
]


def main() -> int:
    print("# GPU runtime checks")
    for label, command in CHECKS:
        print(f"\n## {label}\n{command}")
    print("\n# Optional user-local Python runtime setup")
    for command in SETUP:
        print(command)
    print("\n# Smoke workload")
    for command in SMOKE:
        print(command)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
