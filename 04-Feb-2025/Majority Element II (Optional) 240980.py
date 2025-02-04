# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        m1 = -10^10
        m2 = -10^10

        c1 =0 
        c2 =0


        #searching for two candidates
        for n in nums:

            if(m1==n):
               c1+=1
            elif m2==n:
                c2+=1         
            elif(c1 ==0):
                c1=1
                m1 =n 
            elif(c2 ==0):
                c2=1
                m2 =n 
        
            else:
                c1-=1 
                c2-=1
        #traversing the array performing count to verify if c1 and c2 >n/3


        res =[]

        c1, c2 =0,0

        for n in nums:
            if(m1==n):
                c1+=1
            if(m2 ==n):
                c2+=1
        print(m1, m2)
        if(c1 >(len(nums)/3)):
            res.append((m1))
            
        if(c2 >(len(nums)/3)):
            res.append((m2))
        return res
        


 