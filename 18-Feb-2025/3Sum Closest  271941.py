# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        min_diff = float('inf')
        res =[]
        nums.sort()
        print(nums)

        for i in range(len(nums)):

            l = i+1
            r = len(nums)-1

            while l <r:
                diff = target-(nums[i]+nums[r]+nums[l])

                if abs(diff) < min_diff:
                    min_diff = abs(diff)

                    res =[nums[l], nums[i], nums[r]]
                if diff ==0:
                    return sum(res)

                    l+=1
                    r-=1
                elif diff >0:
                    l+=1
                else:
                    r-=1
            


        return sum(res)
        
