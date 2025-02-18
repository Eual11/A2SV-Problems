# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = Counter()

        # stores the last indices for each character
        for i in range(len(s)):
            last[s[i]] = max(last[s[i]], i)

        #answer is going to appended here
        res =[]


        sub_arr_len =0

        last_idx =0

        for i,ch in enumerate(s):
            last_idx =  max(last_idx, last[ch])
            sub_arr_len+=1

            if(last_idx ==i):
                res.append(sub_arr_len)
                sub_arr_len =0
                
                
        return res
       
