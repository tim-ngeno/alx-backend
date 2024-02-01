#!/usr/bin/env python3
""" LFU caching system """
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    A caching system based on LEast Frequently Used algorithm
    """

    def __init__(self):
        """
        Initializes the LFUCache class, inherited from BaseCaching
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = {}

    def put(self, key, item):
        """
        Assigns the value of item to cache_data based on the `key`
        """
        if key is None or item is None:
            return

        # Update frequency on put
        self.frequency[key] = self.frequency.get(key, 0) + 1

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find Least frequently used item(s)
            min_frequency = min(self.frequency.values())
            items_to_discard = [k for k, v in self.frequency.items() if
                                v == min_frequency]

            # If more than 1 item, use LRU
            if len(items_to_discard) > 1:
                lru_key = min(self.cache_data, key=self.frequency.get)
                items_to_discard = [lru_key]
            for discard_key in items_to_discard:
                if discard_key in self.cache_data:
                    del self.cache_data[discard_key]
                    del self.frequency[discard_key]
                    print('DISCARD: {}'.format(discard_key))

        # Assign new item to cache
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in cache_data linked to the key
        """
        if key is not None and key in self.cache_data:
            # Updata frequency on access
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
