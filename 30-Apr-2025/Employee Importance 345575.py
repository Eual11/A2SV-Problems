# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

from collections import deque
from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        emap = {e.id: e for e in employees}
        if id not in emap:
            return 0

        total_importance = 0
        q = deque([id])

        while q:
            curr_id = q.popleft()
            emp = emap[curr_id]
            total_importance += emp.importance
            q.extend(emp.subordinates)
        
        return total_importance
