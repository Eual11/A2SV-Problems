# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res =[]

        left, top, right, bottom = 0,0, len(matrix[0])-1, len(matrix)-1

        while(left <= right and top <=bottom):

            # from the top to the right

            for i in range(left, right+1):
                res.append(matrix[top][i])
            top+=1

            # moving downwards keeping right most edge


            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1

            # moving to the left from the bottom


            if(top <=bottom):

                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom-=1
                
            if(left <=right):
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])

                left+=1

        return res
        
