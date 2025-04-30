# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

from collections import defaultdict
from typing import List
from functools import lru_cache

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # adjacency list
        tree = defaultdict(list)
        for employee, mgr in enumerate(manager):
            if mgr != -1:
                tree[mgr].append(employee)
        
      
        def dfs(mgr_id: int) -> int:
            if not tree[mgr_id]: 
                return 0
            return informTime[mgr_id] + max(dfs(sub) for sub in tree[mgr_id])
        
        return dfs(headID)
