# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:

        if(key not in self.cache):
            return -1 
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            self.cache.move_to_end(key)
            self.cache[key] = value
        elif(len(self.cache) < self.capacity):
            self.cache[key] = value
        else:
            self.cache.popitem(last=False)
            self.cache[key] = value