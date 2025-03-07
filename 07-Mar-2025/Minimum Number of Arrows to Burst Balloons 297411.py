# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
       points.sort(key=lambda x: x[1]) 

       prev_shoot = points[0][1]
       shoot =1

       for i in range(1, len(points)):
        p = points[i]
        if p[0] <= prev_shoot:
            continue
        else:
            shoot+=1
            prev_shoot = p[1]
       return shoot 