# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       candidates.sort()
       comb =[]
       def solver(path, start, target):
        if target <0:
            return
        if target==0:
            comb.append(path[::]) 
            return
        
        for j in range(start, len(candidates)):
            if  j > start and candidates[j]==candidates[j-1] :
                continue
            path.append(candidates[j])
            solver(path, j+1, target-candidates[j])
            path.pop()

       solver([],0, target) 

       return comb 