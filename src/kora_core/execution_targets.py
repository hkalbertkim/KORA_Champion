"""Execution target labels for KORA Core routing."""

from __future__ import annotations

from kora_core.compat import StrEnum


class ExecutionTarget(StrEnum):
    """Supported v0.1 execution target categories."""

    DETERMINISTIC = "deterministic"
    CACHE = "cache"
    CPU = "cpu"
    LOCAL_GPU = "local_gpu"
    PROVIDER_API = "provider_api"


DETERMINISTIC = ExecutionTarget.DETERMINISTIC
CACHE = ExecutionTarget.CACHE
CPU = ExecutionTarget.CPU
LOCAL_GPU = ExecutionTarget.LOCAL_GPU
PROVIDER_API = ExecutionTarget.PROVIDER_API
