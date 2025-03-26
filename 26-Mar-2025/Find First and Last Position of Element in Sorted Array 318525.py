# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       def lower_bound(arr, target):
        l,r = 0, len(arr)

        while l <r:
            m = l+(r-l)//2

            if arr[m] < target:
                l = m+1
            else:
                r = m
        return l
       def upper_bound(arr, target):
        l, r =0, len(arr)

        while l <r:
            m = l+(r-l)//2

            if arr[m] <= target:
                l = m+1
            else:
                r = m
        return l

       a = lower_bound(nums, target)
       b = upper_bound(nums, target)-1

       if a >=len(nums) or nums[a]!=target:
        a=-1

       if b!=-1 and nums[b]!=target:
        b =-1
       return [a, b]  