# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum =0
        res =[]
        for i in range(0,len(nums)):
            res.append(running_sum+nums[i])
            running_sum+=nums[i]
        return res