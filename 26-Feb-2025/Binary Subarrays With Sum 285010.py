# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

from itertools import accumulate
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
       count =0 
       sum_idx =defaultdict(int)
       sum_idx[0] =1
       n_l = accumulate(nums)
       k = goal
       for n in n_l:

        if n-k in sum_idx:
            count+=sum_idx[n-k]
        sum_idx[n]+=1
       return count 
