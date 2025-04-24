# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        INF = 2**31 -1
        #transforming the grid to a set of distances from rotten oraanges
        M = len(grid)
        N = len(grid[0])
        for r in range(M):
            for c in range(N):
                if(grid[r][c] == 0):
                    grid[r][c] = -1
                elif(grid[r][c] == 1):
                    grid[r][c] = INF
                elif(grid[r][c] == 2):
                    grid[r][c] = 0

        def BFS(cell):
            Q = deque()
            Q.append(cell)

            while Q:
                u = Q.popleft()
                neighbours = [(u[0]-1, u[1]), (u[0]+1, u[1]),(u[0], u[1]-1),(u[0], u[1]+1)]
                for v in neighbours:
                    r =v[0]
                    c = v[1]

                    if(r>=0 and r<M and c>=0 and c<N):
                        if(grid[r][c] >0 and grid[r][c]> grid[u[0]][u[1]]):
                            grid[r][c] = grid[u[0]][u[1]]+1
                            Q.append((r,c))
        for r in range(M):
            for c in range(N):
                if(grid[r][c] == 0):
                    BFS((r,c))

        time =0
        for row in grid:
            time = max(time, max(row))
        if(time == INF):
            return -1
        return time
