# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        uniq = set()
        l =0
        max_len =0

        for r in range(len(s)):
            while s[r] in uniq:
                uniq.remove(s[l])
                l+=1
            uniq.add(s[r])
            max_len = max(max_len, len(uniq))


        return max_len
        
