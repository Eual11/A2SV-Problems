# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans =[0]*len(temperatures)

        stk =[]

        for i in range(len(temperatures)):
            if stk!=[]:
                while stk!=[] and temperatures[stk[-1]] < temperatures[i]:
                    a = stk.pop()
                    ans[a]= i-a
            stk.append(i)

        return ans
        