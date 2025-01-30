# Problem: Convert the Temperature - https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rt_prefix = ""
        prefix_idx =0
        max_str = min(strs, key=len)
        max_ln = len(max_str)
        while(prefix_idx <max_ln):
            if(prefix_idx < len(max_str)):
                prefix = max_str[prefix_idx]
                for string in strs:
                    if(prefix_idx>=len(string)):
                        return rt_prefix 
                    if(string[prefix_idx]!=prefix):
                        return rt_prefix
            else:
                break
            rt_prefix+=prefix
            prefix_idx+=1

        return rt_prefix
