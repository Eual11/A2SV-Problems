# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb =[]

        def solve(path, i, n,k):
            if len(path)==k:
                comb.append(path[::])
                return
            
            for j in range(i+1, n+1):
                path.append(j)
                solve(path, j, n, k)
                path.pop()
        for i in range(1, n+1):
            solve([i], i, n, k)

        return comb