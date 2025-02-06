# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/


from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """

            rotating an image 90 deg horizotnally is basicallt Transpose -> reverse each row
        """

        # transpose matrix first

        n = len(matrix[0])
        for i in range(n):
            for j in range(i, n):
                print(f"({i, j})m ({j, i})")
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse each row


        for row in matrix:
            row.reverse()

