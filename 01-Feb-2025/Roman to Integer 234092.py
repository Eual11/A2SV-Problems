# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
       val_map = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        } 

       res = 0

       l = list(s)

       for i in range(len(l)):
            c = l[i]
            if(i < len(l)-1):
                b = l[i+1]
                if(val_map[c] < val_map[b]):
                    res-=val_map[c]
                else:
                    res+=val_map[c]
            else:
                res+=val_map[c]

      
       return res