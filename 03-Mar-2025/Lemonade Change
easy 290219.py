# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
       changes = {5:0, 10:0, 20:0}
  

       for n in bills:
        if n ==5:
            changes[n]+=1
        elif n==10:
            if changes[n-5]:
                changes[n-5]-=1
                changes[n]+=1
            else:
                return False
        elif n==20:
            if changes[5]>=1 and changes[10]>=1:
                changes[10]-=1
                changes[5]-=1
            elif changes[5]>=3:
                changes[5]-=3
            else:
                return False

       return True