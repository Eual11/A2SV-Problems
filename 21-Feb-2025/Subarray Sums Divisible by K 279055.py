# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        P = defaultdict(int)
        P[0] =1
        cnt =0
        acc=0

        for num in nums:
            acc+=num
            # d = (acc%k + k)%k
            d = acc%k
            if d in P:
                cnt+=P[d]
            P[d]+=1

        return cnt
        