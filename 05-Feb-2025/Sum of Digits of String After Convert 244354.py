# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        transformed =0
        s = "".join([str(ord(i)-96) for i in s])
        print(s)
        for _ in range(k):
            s = str(sum([int(i) for i in s]))
        return int(s)
 