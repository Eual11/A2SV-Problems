# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

from collections import deque, defaultdict
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        leaves = deque([i for i in range(n) if len(graph[i]) == 1])
        
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_length = len(leaves)
            remaining_nodes -= leaves_length
            for _ in range(leaves_length):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)
        
        return list(leaves)
