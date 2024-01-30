#!/usr/bin/env python3
""" Basic Caching module """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system that inherits from the BaseCaching class
    """

    def __init__(self):
        """
        Initializes the BasicCache class.
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns an item with key, value to the dictionary cache_data.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value stored in cache_data linked to key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
