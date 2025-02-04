# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/

import random 

class RandomizedSet:

    def __init__(self):
        self.data =[]
        self.rand_dict ={}
        

    def insert(self, val: int) -> bool:
        if(val not in self.rand_dict):
            self.rand_dict[val] = len(self.data)
            self.data.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:

        if(val in self.rand_dict):
            removed_idx = self.rand_dict[val]
            self.rand_dict[self.data[-1]] = removed_idx
            self.data[-1], self.data[removed_idx] = self.data[removed_idx], self.data[-1]
            self.data.pop()
            del self.rand_dict[val]
            return True

        return False
        

    def getRandom(self) -> int:

        return random.choice(self.data)
        


