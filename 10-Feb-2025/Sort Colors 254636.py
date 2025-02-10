# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count =[0]*3

        # counting


        for c in nums:
            count[c]+=1

        i=0
        j=0
        while(i < len(nums)):

            while(count[j]):
                nums[i] = j
                count[j]-=1
                i+=1
            j+=1
