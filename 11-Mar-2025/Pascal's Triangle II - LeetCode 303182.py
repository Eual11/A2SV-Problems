# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        fact_lst =[]

        for k in range(rowIndex+1):
            fact_lst.append(int((math.factorial(rowIndex))/((math.factorial(k)*math.factorial(rowIndex-k)))))
        return fact_lst
