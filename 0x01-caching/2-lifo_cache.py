#!/usr/bin/python3
"""LIFO Cache Module

The LIFOCache class implements the Last-In, First-Out (LIFO)
eviction policy, discarding the most recently added item when the cache is
full.

"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache is a caching system that inherits from BaseCaching.

    This caching system implements the (Last-In, First-Out) eviction policy.
    """

    def __init__(self):
        """Initialize the LIFO cache."""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            last_item_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_item_key]
            print("DISCARD:", last_item_key)

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
