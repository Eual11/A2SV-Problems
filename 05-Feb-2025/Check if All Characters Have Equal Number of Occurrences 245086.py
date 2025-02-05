# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        letters =[0]*26

        for c in s:
            letters[ord(c)-97]+=1
        v =None
        for c in letters:
            if c!=0:
                if not v:
                    v = c
                elif c!=v:
                    return False
            
        return True