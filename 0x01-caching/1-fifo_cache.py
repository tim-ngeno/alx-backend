#!/usr/bin/env python3
""" FIFO caching module """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A caching system for FIFO algorithm
    """

    def __init__(self):
        """
        Initializes the FIFOCache class with the cached data from the
        base class
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns to `item` the value corresponding to the `key` attribute
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the first item in cache (FIFO)
            discarded_key = next(iter(self.cache_data.keys()))
            self.cache_data.pop(discarded_key)
            print('DISCARD: {}'.format(discarded_key))

        # Assign the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in cached_data associated with `key`
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
