# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
       l =0
       r = n

       while l <r:
        m = l+(r-l)//2

        if not isBadVersion(m):
            l = m+1
        else:
            r = m

       return l 