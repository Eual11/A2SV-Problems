# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res, part = [], []

        def dfs(i):
            if i == len(s):
                if len(part)==4:
                    res.append(".".join(part.copy()))
                    return
            for j in range(i, len(s)):
                
                if self.isvalid(s, i, j+1):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res
        

    def isvalid(self,s,i,j):
        substr = s[i:j]
        if not substr or len(substr) > 3:
            return False
        if substr[0] == '0' and len(substr) > 1:
            return False
        return substr.isdigit() and 0 <= int(substr) <= 255