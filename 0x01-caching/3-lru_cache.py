#!/usr/bin/python3
"""LRU Cache Module

The LRUCache class implements the Least Recently Used (LRU) eviction policy,
discarding the least recently accessed item when the cache is full.

"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    This caching system implements the Least Recently Used eviction policy.
    """

    def __init__(self):
        """Initialize the LRU cache."""
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
            lru_key = self.access_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

    def get(self, key):
        """Get an item by key."""
        if key is None or key not in self.cache_data:
            return None

        self.access_order.remove(key)
        self.access_order.append(key)

        return self.cache_data[key]
