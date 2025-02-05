# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        transformed =0
        s = "".join([str(ord(i)-96) for i in s])
        print(s)
        for _ in range(k):
            s = str(sum([int(i) for i in s]))
        return int(s)
 