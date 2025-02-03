# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sum =0

        is_zero = False

        for n in nums:
            sum+=n
            if(n == 0):
                is_zero = True 
        if(not is_zero):
            return 0
        n = len(nums)
        return (int(n*(n+1)/2))-sum
 