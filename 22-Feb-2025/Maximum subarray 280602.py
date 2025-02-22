# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')

        cur_sum =0

        for n in nums:
            cur_sum+=n
            max_sum = max(cur_sum, max_sum)
            if cur_sum<0:
                cur_sum =0

        return max_sum