# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict = {num: i for i, num in enumerate(nums)}
        
        for i,n in enumerate(nums):
            if((target - n) in nums_dict and nums_dict[target-n]!=i):
                return [i, nums_dict[target-n]]
        return []
 