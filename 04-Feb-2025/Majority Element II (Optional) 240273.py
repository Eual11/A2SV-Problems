# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [i for i in [w for w, o in Counter(nums).most_common() if o >(len(nums)/3)]]