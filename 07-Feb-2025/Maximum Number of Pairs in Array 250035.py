# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs =0
        cntr = Counter(nums)

        for v in cntr.values():
            pairs+=(v//2)

        return [pairs, len(nums)-2*pairs]

        