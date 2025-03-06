# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        B = 0
        cnt =0

        for c in s:
            if c =='L':
                B+=1
            else:
                B-=1
            if B==0:
                cnt+=1

        return cnt
            