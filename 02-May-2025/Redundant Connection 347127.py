# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self, n) -> None:
                self.parent = list(range(n+1))
                self.size = [0]*(n+1)
            def find(self, v)-> int:
                if(v == self.parent[v]):
                    return v
                else:
                    self.parent[v] = self.find(self.parent[v])
                    return self.parent[v]
            def union(self, a, b)->bool:
                a = self.find(a)
                b = self.find(b)

                if(a!=b):
                    if(self.size[a] <self.size[b]):
                        a, b = b, a
                    self.parent[b] = a
                    self.size[a]+=1
                    return True

                return False
        uf =  UnionFind(len(edges))
        # lst = []
        for u,v in edges:
            if( not uf.union(u, v)):
                return [u,v]
        # return lst[-1]