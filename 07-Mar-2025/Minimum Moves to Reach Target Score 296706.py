# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """

        moves =0

        while target!=1:
            if maxDoubles ==0:
                moves+=(target-1)
                target =1
            elif maxDoubles >0 and target%2==0:
                target//=2
                maxDoubles-=1
                moves+=1
            else:
                target-=1
                moves+=1


        return moves
        