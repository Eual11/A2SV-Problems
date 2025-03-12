# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        can_win = False

        def solve(s, e, t):
            if s==e:
                return nums[s]
            L = nums[s]-solve(s+1, e, -t)
            R = nums[e]-solve(s,e-1,-t)
            
            return max(L, R)
            
        return solve(0, len(nums)-1, 1) >=0



