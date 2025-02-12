# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        write = 1

        for read in range(1,len(nums)):
           if(nums[read] != nums[read-1]):
               nums[write] = nums[read]
               write+=1

        return write
