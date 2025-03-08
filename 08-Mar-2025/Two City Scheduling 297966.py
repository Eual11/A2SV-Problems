# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda x: (x[0]-x[1])) 

        s =0
        n=len(costs)//2

        for i in range(n):
            s+=costs[i][0]
        for i in range(n, 2*n):
            s+=costs[i][1]
        return s