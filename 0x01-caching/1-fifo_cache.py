#!/usr/bin/python3
"""FIFO Cache Module

The FIFOCache class implements the First-In, First-Out (FIFO)
eviction policy, discarding the oldest item when the cache is full.

"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache is a caching system that inherits from BaseCaching.

    This caching system implements the (First-In, First-Out) eviction policy.
    """

    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = next(iter(self.cache_data))
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
