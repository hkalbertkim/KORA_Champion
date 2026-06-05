"""Compatibility helpers for supported Python runtimes."""

from __future__ import annotations

try:
    from enum import StrEnum
except ImportError:  # Python 3.10
    from enum import Enum

    class StrEnum(str, Enum):
        pass


__all__ = ["StrEnum"]
