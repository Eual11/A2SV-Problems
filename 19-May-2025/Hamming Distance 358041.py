# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        ham_dist =0

        while (x or y ):
            ham_dist +=int((x&1)!=(y&1))

            x>>=1; y>>=1


        return ham_dist
        