# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count =0
        for w in words:
            for c in w:
                if(c not in allowed_set):
                    break
            else:
                count+=1
        return count