"""
Problem 1: Least Recently Used Cached
"""

from collections import (OrderedDict, )

class LRU_Cache(object):

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        val = self.cache.get(key, -1)
        if val != -1:
            # O(1) time complexity ( python >= 3.2 )
            self.cache.move_to_end(key, last=False)
        return val

    def set(self, key, value):
        if self.capacity == 0:
            print("Capacity = 0: invalid operation")
            return
        
        cache_hit = (self.cache.get(key, None) is not None )
        print(f"Cache hit: {cache_hit}")

        if cache_hit:
            self.cache.move_to_end(key, last=False)
        else:
            """
            add the key to the cache
            """

            # only add if there's still space available
            if len(self.cache) < self.capacity:
                self.cache[key] = value            
            else:
                self.cache.popitem(last=False)
                self.cache[key] = value

# testing
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2) 
our_cache.set(3, 3) 
our_cache.set(4, 4) 


assert our_cache.get(1) == 1,"should returns 1"
assert our_cache.get(2) == 2,"should returns 2"
assert our_cache.get(9) == 1,"should returns -1 because 9 is not present in the cache"

our_cache.set(5, 5)  
our_cache.set(6, 6)

assert our_cache.get(3) == -1, "should returns -1 because the cache reached it's capacity and 3 was the least recently used entry"
