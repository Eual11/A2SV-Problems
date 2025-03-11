# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stk =[0]

        for c in s:
            if c =="(":
                stk.append(0)
            else:
                a = stk.pop()
                a = max(2*a, 1)
                stk[-1]+=a
        return stk[0]

        