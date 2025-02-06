# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row/column checking
        for i in range(9):
            sr =Counter([board[i][j] for j in range(9)])
            sc = Counter([board[j][i] for j in range(9)])
            most_common = sr.most_common(2)
            if(most_common[0][0]!="." and most_common[0][1]>1):
                return False

            if(len(most_common) >1 and most_common[1][1]>1):
                return False
            most_common = sc.most_common(2)
            if(most_common[0][0]!="." and most_common[0][1]>1):
                return False
            if(len(most_common) >1 and most_common[1][1]>1):
                return False





        #grid checking
        for i in range(0, 9, 3):
            for j in range(0,9,3):
                st =Counter( [
                    board[i][j],board[i][j+1], board[i][j+2],
                    board[i+1][j], board[i+1][j+1], board[i+1][j+2],
                    board[i+2][j], board[i+2][j+1], board[i+2][j+2]
                ])
                most_common = st.most_common(2)
                if(most_common[0][0]!="." and most_common[0][1]>1):
                    return False
                if(len(most_common) >1 and most_common[1][1]>1 ):
                    return False

        return True

