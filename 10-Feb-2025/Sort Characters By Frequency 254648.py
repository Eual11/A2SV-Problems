# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:

        c = Counter(s)

        return "".join( [s*v for s, v in c.most_common(len(s))])

        
 