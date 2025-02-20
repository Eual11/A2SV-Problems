# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

from itertools import accumulate
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        c_list = list(map(lambda x: ord(x)-ord('a'), s))

        D = [0]*len(c_list)

        for l,r, k in shifts:
            D[l]+= (1 if k==1 else -1)
            if r+1 < len(c_list):
                D[r+1]-= (1 if k==1 else -1)
        D = list(accumulate(D))
        result = [

            chr(((c_list[i]+D[i])%26)+ord('a')) for i in range(len(D))
        ]
        return "".join(result)