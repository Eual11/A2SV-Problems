# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution(object):
    def trailingZeroes(self, n):

        if n <5:
            return 0
        return n//5 +self.trailingZeroes(n//5)