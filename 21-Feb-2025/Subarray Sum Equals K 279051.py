# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sum_idx = defaultdict(int)
        sum_idx[0] = 1
        cnt =0
        acc =0

        for num in nums:
            acc+=num

            d = acc-k
            if d in sum_idx:
                cnt+=sum_idx[d]
            sum_idx[acc]+=1
            

        return cnt

        
        