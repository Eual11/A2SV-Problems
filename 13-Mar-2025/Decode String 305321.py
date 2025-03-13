# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stk =[]
        j =0

        while j < len(s):
            c = s[j]
            if c.isdigit():
                n = ""
                while j < len(s) and s[j].isdigit():
                    n+=s[j]
                    j+=1
                print(n)
                stk.append(n)
                
            elif c =="[":
                j+=1
            elif c =="]":
                d =""

                while stk!=[] and not stk[-1].isdigit():
                    d = stk.pop()+d
                if stk !=[]:
                    i = int(stk.pop())
                    stk.append(d*i)
                j+=1
            else:
                stk.append(c)
                j+=1



        return "".join(stk)
        

