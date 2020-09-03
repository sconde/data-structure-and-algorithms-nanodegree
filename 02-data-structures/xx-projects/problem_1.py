"""
Problem 1: Least Recently Used Cached
"""
from collections import (OrderedDict,)


class LRUCache:

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        val = self.cache.get(key)
        if val:
            # O(1) time complexity ( python >= 3.2 )
            self.cache.move_to_end(key, last=False)

        return val

    def set(self, key, value):
        if self.capacity == 0:
            print("Capacity = 0: invalid operation")
            return

        cache_hit = self.cache.get(key) is not None
        print("cache hit = ", cache_hit)
        if cache_hit:
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value
            else:
                self.cache.popitem(last=False)
                self.cache[key] = value



# testing
our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2) 
our_cache.set(3, 3) 
our_cache.set(4, 4) 

print(our_cache.get(1))
print(our_cache.get(2))
print(our_cache.get(9))
our_cache.set(5, 5)  
our_cache.set(6, 6)
print(our_cache.get(3))


# review - case
review_cache = LRUCache(5)
review_cache.set(1, 1)
print(review_cache.get(2) ) # returns -1
review_cache.set(1, 11111)
print(review_cache.get(1))  # overriding a value, returns 11111