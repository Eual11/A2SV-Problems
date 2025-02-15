# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum =0
        res =[]

        for c in nums:
            if(c%2==0):
                even_sum+=c
        print(even_sum)
        for q in queries:
            n = nums[q[1]]
            val = q[0]
            if(n%2==0):
                even_sum-=n
            if((n+val)%2==0):
                even_sum+=(n+val)
            nums[q[1]]+=val
            res.append(even_sum)
        return res
        
