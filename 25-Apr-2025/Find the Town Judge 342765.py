# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if(trust==[] and n>1):
            return -1
        d ={}
        
        for i in range(1, n+1):
            d[i] = []
        for k in trust:
            d[k[0]].append(k[1])
        print(d)

        num_cynic = 0 
        cynic = -1
        for i in range(1, n+1):
            if(d[i] ==[]):
                num_cynic+=1
                cynic = i
        # print(num_cynic)
        if(num_cynic !=1):
            return -1
        # print(cynic)
        for i in range(1, n+1):
            if(cynic not in d[i] and d[i]!=[]):
                return -1
        return cynic