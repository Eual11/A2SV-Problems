# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        s_ctr = Counter(s2[:k])
        t_ctr = Counter(s1)


        for i in range(k, len(s2)):
            if(s_ctr == t_ctr):
                return True
            s_ctr[s2[i-k]]-=1

            if(s_ctr[s2[i-k]] ==0):
                del s_ctr[s2[i-k]]
            s_ctr[s2[i]]+=1


        return s_ctr==t_ctr

        
