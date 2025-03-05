# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = sorted([a for a in s], reverse=True)
        s.remove('1')
        s.append('1')
        return "".join(s)
