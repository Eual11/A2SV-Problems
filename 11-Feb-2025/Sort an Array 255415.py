# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def shell_sort(nums):

            gap = len(nums)//2
            while gap:

                for i in range(gap, len(nums)):
                    x = nums[i]
                    j = i
                    while j >=gap and nums[j-gap] > x:
                        nums[j] = nums[j-gap]
                        j-=gap
                    nums[j] = x

                gap//=2

            return nums
        return shell_sort(nums)

        
        
