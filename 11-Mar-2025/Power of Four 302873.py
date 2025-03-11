# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution(object):
    def isPowerOfFour(self, n):
       
       if n==1:
        return True
       if n <4:
        return False 
       return n%4==0 and self.isPowerOfFour(n//4)   