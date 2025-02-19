# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/


class Solution:
    def minimumSteps(self, s: str) -> int:
       num_black_right =0

       num_swamps =0

       for c in s:
           if(c=="1"):
               num_black_right+=1
           else:
               num_swamps+=num_black_right


       return num_swamps
