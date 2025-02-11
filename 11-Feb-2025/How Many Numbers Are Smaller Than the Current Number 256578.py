# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        index_map ={}

        for i,c in enumerate(sorted_nums):
            if c not in index_map:
                index_map[c] =i
        print(index_map)
            

        return [index_map[num] for num in nums]