# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def capacity(cp):

            days_count =0
            sum =0
            last_idx =0
            # print(cp)
            while(last_idx < len(weights)):
                if(weights[last_idx] <=cp):
                    while( last_idx < len(weights) and sum+weights[last_idx] <= cp):
                        # print(weights[last_idx], end=", ")
                        sum+=weights[last_idx]
                        last_idx+=1
                    # print()
                    sum=0
                    days_count+=1
                else: return False
            return days_count<=days
        lo =0
        hi = sum(weights)

        while(lo < hi):
            m = lo+(hi-lo)//2
            if(capacity(m)):
                hi = m
            else: 
                lo = m+1
        return lo 

