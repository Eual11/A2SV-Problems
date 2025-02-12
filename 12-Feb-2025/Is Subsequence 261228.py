# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        r = 0

        for i in range(len(t)):
            if(r ==len(s)):
                break
            if(s[r] == t[i]):
                r+=1

        return r == len(s)