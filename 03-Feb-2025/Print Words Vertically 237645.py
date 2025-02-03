# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        res =[]
        s_list = s.split()
        max_len = len(max(s_list, key=len))
        for i in range(max_len):
            r = "".join([c[i] if len(c) >i else ' ' for c in s_list])
            res.append(r.rstrip())
        return res
 