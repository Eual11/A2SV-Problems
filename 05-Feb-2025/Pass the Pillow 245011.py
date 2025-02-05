# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        trip = (n-1)*2  
        r = time % trip
        if r <(n-1):
            return r +1
        else:
            return n-(r-(n-1)) 

