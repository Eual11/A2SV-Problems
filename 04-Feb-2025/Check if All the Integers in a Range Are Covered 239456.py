# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        check = [False]*51

        for start, end in ranges:
            for i in range(start, end+1):
                check[i] = True
        return all([check[i] for i in range(left, right+1)])
