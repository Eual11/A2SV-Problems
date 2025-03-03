# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_sum= 0
        n = len(nums)

        for i in range(n-2):

            seg = nums[i:i+3]
            # print(seg)
            if nums[i]+nums[i+1] > nums[i+2]:
                max_sum = max(sum(seg), max_sum)


        return max_sum