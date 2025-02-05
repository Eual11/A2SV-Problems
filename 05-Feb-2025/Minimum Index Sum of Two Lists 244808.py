# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

from typing import List
from collections import Counter
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        c1 = Counter(list1)
        c2 = Counter(list2)


        min_idx = float("inf")

        res = []
        for s in list1:
            if(c1[s] and c2[s]):
                i = list1.index(s)
                j = list2.index(s)
                idx = i+j
                if(idx <= min_idx):
                    res.append((s, idx))
                    min_idx = idx
        return [w for w, i in res if i==min_idx]


            
    
    