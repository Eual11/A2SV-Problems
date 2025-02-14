# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
       left= 0
       min_substr =""
       i =0
       len_substr = float('inf')
       
       t_ctr = Counter(t)
       s_ctr = Counter()

       def validate(s,t)->bool:

           for c in t.keys():
               if(s[c] < t[c]):
                   return False
           return True

       for right in range(len(s)):
           s_ctr[s[right]]+=1
           while(validate(s_ctr, t_ctr)):

               if(right-left+1 < len_substr):
                   len_substr = right-left+1
                   i=left
               s_ctr[s[left]]-=1 
               if(s_ctr[s[left]]==0):
                   del s_ctr[s[left]] 
               left+=1
       if(len_substr == float('inf')):
           return "" 
       return s[i: i+int(len_substr)]
                          
           



       

        
           
