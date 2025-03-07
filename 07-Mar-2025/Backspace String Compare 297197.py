# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        A = []
        B =[]

        for c in s:
            if c=="#" and A!=[]:
                A.pop()
            elif c!="#":
                A.append(c)
        for c in t:
            if c=="#" and B!=[]:
                B.pop()
            elif c!="#":
                B.append(c)
        return A==B
   
        