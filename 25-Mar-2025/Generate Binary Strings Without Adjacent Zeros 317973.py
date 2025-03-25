# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:

       ans =[] 

       def backtrack(s):
        if(len(s)==n):
            ans.append(s[::])
            return
        if(s[-1]=="0"):
            backtrack(s+"1")
        else:
            backtrack(s+"0")
            backtrack(s+"1")

       backtrack("1")
       backtrack("0")  


       return ans


