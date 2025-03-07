# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stk =[]

        for o in logs:
            if o=="../" and stk!=[]:
                stk.pop()
            elif o!="../" and o !="./":
                stk.append(o)
        return len(stk)
        