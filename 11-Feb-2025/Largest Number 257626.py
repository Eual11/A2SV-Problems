# Problem: Largest Number - https://leetcode.com/problems/largest-number/

#[111311,1113]
# [91,9]
#
# 

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):

                a = str(nums[j])
                b = str(nums[j+1])

                if(int(a+b) < int(b+a)):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int("".join(map(str, nums))))