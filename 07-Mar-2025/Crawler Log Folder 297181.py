# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        depth =0

        for c in logs:
            if c =="../":
                depth = max(0, depth-1)
            elif c!='./':
                depth+=1
        return depth