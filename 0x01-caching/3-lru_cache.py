#!/usr/bin/env python3
""" Least Recently Used Caching """
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    A caching system implementing LRU
    """

    def __init__(self):
        """
        Initializes LRUCache class that inherits from BaseCaching
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assigns `item` with value associated with `key` to `cache_data`
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = next(iter(self.cache_data.keys()))
            self.cache_data.pop(discarded_key)
            print('DISCARD: {}'.format(discarded_key))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Returns the value in cache_data linked to `key`
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
