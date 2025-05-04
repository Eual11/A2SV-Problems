# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        op_count =0

        while nums[0] < k:

            a = heappop(nums)
            b = heappop(nums)
            heappush(nums, min(a, b)*2 +max(a, b))
            op_count+=1
        return op_count
        
