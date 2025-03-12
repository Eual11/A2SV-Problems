# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution(object):
    def simplifyPath(self, path):
       
       dirs = path.split('/') 
       final =['']

       for d in dirs:
        d.replace("/", "")

        if d=="..":
            if final!=[] and final[-1]!="":
                final.pop()
        elif d=="." or d=="":
            continue
        else:
            final.append(d)

       f = "/".join(final)
       if f=="//" or f=="":
        return "/"
       return f 