# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

       prefix_prod = [1]*len(nums)
       suffix_prod = [1]*len(nums)


       res =[1]*len(nums)


       for i in range(1, len(nums)):

           prefix_prod[i] = nums[i-1]*prefix_prod[i-1]
       for i in range(len(nums)-2, -1, -1):

           suffix_prod[i] = suffix_prod[i+1]*nums[i+1]
       return [prefix_prod[i]*suffix_prod[i] for i in range(len(nums))]
        
    
               


           
