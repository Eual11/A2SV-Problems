# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        index =0
        p = list(range(1, n+1))

        while len(p)>1:
            index = (index+(k-1))%len(p)
            p.pop(index)
        return p[0]