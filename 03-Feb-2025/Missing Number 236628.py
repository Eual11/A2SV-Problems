# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

from functools import reduce
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        return reduce( lambda x,y:x ^y, nums) ^ reduce(lambda x, y:x^y, list(range(len(nums)+1)))

 