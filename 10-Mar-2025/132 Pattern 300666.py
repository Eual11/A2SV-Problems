# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stk =[]
        nk = float('-inf')

        for i in range(len(nums)-1, -1,-1):

            if nums[i] < nk:
                return True
            while stk!=[] and stk[-1] < nums[i]:
                nk = stk.pop()
            stk.append(nums[i])
        return False

