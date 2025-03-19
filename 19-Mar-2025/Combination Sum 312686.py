# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

       comb =[]
       n = len(candidates)
       def solve(path, i, target):
        if target <0:
            return
        if target==0:
            comb.append(path[::])
            return
        
        for j in range(i, len(candidates)):
            path.append(candidates[j])
            solve(path, j, target-candidates[j])
            path.pop()
       for i in range(len(candidates)):
        num = candidates[i]
        solve([num], i, target-num) 

       return comb 
