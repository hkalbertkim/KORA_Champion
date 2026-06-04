"""Small deterministic cache helpers for local benchmark runs."""

from __future__ import annotations

import hashlib
import json
from collections import OrderedDict
from dataclasses import dataclass
from typing import Any, Mapping


def build_cache_key(namespace: str, payload: Mapping[str, Any]) -> str:
    """Build a stable cache key from a namespace and JSON-like payload."""

    serialized = json.dumps(
        {"namespace": namespace, "payload": payload},
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    )
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class CacheLookup:
    """Result of a cache lookup."""

    hit: bool
    key: str
    value: Any = None


class InMemoryCache:
    """Bounded in-memory cache for synthetic local harnesses."""

    def __init__(self, *, max_entries: int = 1000) -> None:
        self._items: OrderedDict[str, Any] = OrderedDict()
        self._max_entries = max(1, int(max_entries))

    def get(self, key: str) -> CacheLookup:
        if key not in self._items:
            return CacheLookup(hit=False, key=key)
        self._items.move_to_end(key)
        return CacheLookup(hit=True, key=key, value=self._items[key])

    def set(self, key: str, value: Any) -> None:
        self._items[key] = value
        self._items.move_to_end(key)
        while len(self._items) > self._max_entries:
            self._items.popitem(last=False)

    def clear(self) -> None:
        self._items.clear()

    def __len__(self) -> int:
        return len(self._items)
