# Problem: 3Sum - https://leetcode.com/problems/3sum/description/


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res =[]


        # sorting nums to perform two sum with target -a for a in nums
        nums.sort()
        print(nums)
        for i  in range(len(nums)):

            # jumping to avoid duplicate tripletes
            if(i>0 and nums[i-1] == nums[i]):
                continue

            target = nums[i]

            l = i+1
            r = len(nums)-1

            while l <r:

                total = nums[l]+nums[r]+target
                if(total ==0):
                    res.append([nums[l], nums[i], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while r >l and nums[r] == nums[r+1]:
                        r-=1
                elif total <0:
                    l+=1
                else:
                    r-=1



        return res
