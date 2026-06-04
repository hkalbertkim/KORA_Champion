import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from kora_core.cache import InMemoryCache, build_cache_key


class CacheTests(unittest.TestCase):
    def test_cache_key_is_stable(self) -> None:
        left = build_cache_key("request", {"b": 2, "a": 1})
        right = build_cache_key("request", {"a": 1, "b": 2})
        self.assertEqual(left, right)

    def test_cache_hit_and_miss(self) -> None:
        cache = InMemoryCache()
        self.assertFalse(cache.get("missing").hit)
        cache.set("alpha", {"value": 1})
        lookup = cache.get("alpha")
        self.assertTrue(lookup.hit)
        self.assertEqual(lookup.value, {"value": 1})

    def test_cache_stores_and_retrieves_values(self) -> None:
        cache = InMemoryCache(max_entries=1)
        cache.set("alpha", "one")
        self.assertEqual(cache.get("alpha").value, "one")
        cache.set("beta", "two")
        self.assertFalse(cache.get("alpha").hit)
        self.assertEqual(cache.get("beta").value, "two")


if __name__ == "__main__":
    unittest.main()
