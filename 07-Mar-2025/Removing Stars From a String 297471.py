# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk =[]

        for c in s:
            if c =="*":
                if stk!=[]:
                    stk.pop()
            else:
                stk.append(c)



        return "".join(stk)
        