# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

from itertools import accumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:   
        return  list(accumulate(nums))