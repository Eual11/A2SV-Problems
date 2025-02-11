# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        steps_count = len(piles)//3

        coins =0

        t = len(piles)-1

        i=1

        while(i <t):
            coins+=piles[i]
            i+=2
            t-=1


        return coins