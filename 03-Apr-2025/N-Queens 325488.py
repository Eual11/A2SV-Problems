# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
      
        result =[]
        def register_board(board, n):
            new_board = ["."*n]*n
            for q in board:
                row = list(new_board[q[0]])
                row[q[1]] = "Q"
                new_board[q[0]] = "".join(row)
            result.append(new_board)
        def isValid(cell, board):
            for q in board:
                if(q[0] == cell[0] or q[1] == cell[1] \
                    or abs(q[0]- cell[0]) == abs(q[1] - cell[1])
                       ):
                    return False 
            return True

        def solve(board, row, n):
            if(row == n):
                register_board(board, n)
            for col in range(n):
                if(isValid((row, col), board)):
                    board.append((row, col))
                    solve(board, row+1, n)
                    board.pop()

        solve([], 0, n)

        return result 

