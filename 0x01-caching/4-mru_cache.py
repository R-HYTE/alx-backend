#!/usr/bin/python3
"""MRU Cache Module

The MRUCache class implements the Most Recently Used (MRU)
eviction policy,
discarding the most recently accessed item when the cache is full.

"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache is a caching system that inherits from BaseCaching.

    This caching system implements the Most Recently Used eviction policy.
    """

    def __init__(self):
        """Initialize the MRU cache."""
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.access_order.remove(key)

        self.cache_data[key] = item
        self.access_order.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            mru_key = self.access_order.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

    def get(self, key):
        """Get an item by key."""
        if key is None or key not in self.cache_data:
            return None

        self.access_order.remove(key)
        self.access_order.append(key)

        return self.cache_data[key]
