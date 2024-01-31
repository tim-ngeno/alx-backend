#!/usr/bin/env python3
""" MRU caching system """

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    A caching system based on Most Recently Used mechanism
    """

    def __init__(self):
        """
        Initializes the MRUCache class inherited from BaseCaching
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assigns the value of `item` to cache_data based on the `key`
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key, _ = self.cache_data.popitem()
            print('DISCARD: {}'.format(discarded_key))

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Returns the value in cache_data linked to key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
