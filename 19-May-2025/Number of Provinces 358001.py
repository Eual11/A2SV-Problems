# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:


        num_prov =0
        N = len(isConnected)
        vistied = set()
        def dfs(node):
            vistied.add(node)

            for v in range(N):
                if(isConnected[node][v] and v not in vistied):
                    dfs(v)


        for c in range(N):
            if(c not in vistied):
                dfs(c)
                num_prov+=1
        return num_prov
        