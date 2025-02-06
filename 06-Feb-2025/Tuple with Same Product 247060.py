# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

from collections import Counter
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_dict = Counter()
        ans = 0
        n = len(nums)
        for i in range(n):
           for j in range(i+1, n):
            prod = nums[i] * nums[j]
            ans += 8*prod_dict[prod]
            prod_dict[prod]+=1
        return ans

                
	        
