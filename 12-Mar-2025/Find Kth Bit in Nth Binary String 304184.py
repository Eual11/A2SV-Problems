# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            return "".join(["0" if c =="1" else "1" for c in s])
        def reverse(s):
            a = s
            a.reverse

        def sol(i):
            if i==1:
                return "0"
            else:
                return sol(i-1)+"1"+invert(sol(i-1))[::-1]
        A = sol(n)
        return A[k-1]
