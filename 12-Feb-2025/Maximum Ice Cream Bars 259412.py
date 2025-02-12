# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        #approah sort the costs in increasing manenr
        # start from the least expensive to the most expensive

        costs.sort()


        count =0

        i=0
        while(coins >0 and  i < len(costs)):

            if(costs[i] <= coins):
                count+=1
                coins-=costs[i]

            i+=1


        return count
        
