# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/

import random
class RandomizedSet:

    def __init__(self):
        self.rand_dict={}
        self.data = []       

    def insert(self, val: int) -> bool:
        if(val in self.rand_dict):
            return False

        self.rand_dict[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if(val in self.rand_dict):

            removed_index = self.rand_dict[val]
            self.rand_dict[self.data[-1]] = removed_index
            self.data[self.rand_dict[val]], self.data[-1] =  self.data[-1], self.data[self.rand_dict[val]]
            del self.rand_dict[self.data[-1]]
            self.data.pop()

            return True
        else:
            return False
        

    def getRandom(self) -> int:
       return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
#