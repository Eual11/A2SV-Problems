# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        
    # convert 2D board into  list .
        def get_board_index(val):
            row = (val - 1) // N
            col = (val - 1) % N
            if row % 2 == 1:
                col = N - 1 - col
            return N - 1 - row, col
        
        visited = set()
        queue = deque([(1, 0)])  

        while queue:
            pos, moves = queue.popleft()
            for i in range(1, 7):
                next_pos = pos + i
                if next_pos > N * N:
                    continue
                r, c = get_board_index(next_pos)
                if board[r][c] != -1:
                    next_pos = board[r][c]
                if next_pos == N * N:
                    return moves + 1
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))
        
        return -1
