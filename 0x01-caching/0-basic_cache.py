#!/usr/bin/python3
"""
Basic Cache Module

This module contains the definition of the BasicCache class,
which implements a simple caching system that inherits from BaseCaching.
The BasicCache class allows adding and retrieving items from the cache.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache is a caching system that inherits from BaseCaching

    This caching system has no limit on the number of items it can store.
    """
    def put(self, key, item):
        """Add an item in the cache.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.

        If either key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key.

        Args:
            key: The key for the item to retrieve from the cache.

        Returns:
            The value associated with the key, or None if the key is None or
            does not exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
