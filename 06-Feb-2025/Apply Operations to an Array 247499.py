# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            j = i+1

            if(nums[i] == nums[j]):
                nums[i] = 2*nums[j]
                nums[j] = 0



        l, r = 0, 0

        n = len(nums)
        while(r < n):

            if(nums[r] == 0):
                r+=1
                continue

            else:
                nums[l] = nums[r]
                l+=1
                r+=1

        while(l < n):
            nums[l] = 0
            l+=1
                
        return nums
 