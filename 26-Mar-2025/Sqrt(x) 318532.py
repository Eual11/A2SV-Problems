# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if(x<=1):
            return x
        l = 2
        r = x

        while(l < r):
            m = l+(r-l)//2

            if(m**2 > x):
                r = m 
            else:
                l = m+1
        return r-1

