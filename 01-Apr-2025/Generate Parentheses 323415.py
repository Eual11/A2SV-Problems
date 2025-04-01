# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
       def isValid(s):
        stk =[] 


        for c in s:
            if  c=="(":
                stk.append(c)
            else:
                if len(stk) >0 and stk[-1] =="(":
                    stk.pop()
                else:
                    return False
        return stk==[]


       valid_parn =[]

       def backtrack(s, l, r):
            if l==n and r==n:
                if(isValid(s)):
                    valid_parn.append(s)
            elif l >n or r>n:
                return
            
            backtrack(s+"(", l+1, r)
            backtrack(s+")", l, r+1)
 
       backtrack("", 0, 0)

       return valid_parn






