# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        smallest = 10**10

        def backtrack(s, i):
            nonlocal smallest
            if(i >= len(pattern)):
                int_s = int(s)
                smallest = min(smallest, int_s)
                return
            if(pattern[i]=='I'):
                # handle increasing case
                for c in range(int(s[i])+1, 10):
                    sc = str(c)
                    if sc not in s and i+1 <= len(pattern):
                        backtrack(s+sc, i+1)
            else:
                #handle decreasing case
                for c in range(int(s[i])-1, 0, -1):
                    sc = str(c)
                    if sc not in s and i+1 <= len(pattern):
                        backtrack(s+sc, i+1)

        for i in range(1, 10):
            backtrack(str(i), 0)




        return str(smallest)