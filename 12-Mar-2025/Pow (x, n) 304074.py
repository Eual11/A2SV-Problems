# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def p(x, n):
            if n==0:
                return 1
            if n%2==0:
                return self.myPow(x*x, n//2)
            else:
                return x*self.myPow(x*x, (n-1)//2)
        if n<0:
            return 1.0/(p(x,-n))
        return p(x,n)
        