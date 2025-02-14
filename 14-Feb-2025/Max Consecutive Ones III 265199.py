# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        max_len =0

        left =0
        freq =0

        for right in range(len(nums)):
            if(nums[right]):
                freq+=1

            if(right-left+1 > freq+k):
                if(nums[left]):
                    freq-=1
                left+=1
            max_len = max(max_len, right-left+1)

        

        return max_len        
