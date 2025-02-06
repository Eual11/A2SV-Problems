# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)):
            if( nums[i] ==0):
                j =i+1

                while(j < len(nums)):

                    if(nums[j] !=0):
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    else:
                        j+=1
    
