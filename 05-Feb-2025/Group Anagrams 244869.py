# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dic = {}

        for word in strs:
            c = "".join(sorted(word))
            if( c in group_dic):
                group_dic[c].append(word)
            else:
                group_dic[c] = [word]
        return list(group_dic.values()) 

