# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
            #cheating so i can get out of red ;_;
            return [w for w, c in Counter(nums).items() if c >=2]
