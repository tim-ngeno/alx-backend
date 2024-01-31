#!/usr/bin/env python3
""" LIFO Caching module """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    A LIFO-based caching system
    """

    def __init__(self):
        """
        Initializes LIFOCache that inherits from BaseCaching
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns to the dictionary `cache_data` the item value for the
        the key `key`
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key, _ = self.cache_data.popitem()
            print('DISCARD: {}'.format(discarded_key))
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in cache_data associateed to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
