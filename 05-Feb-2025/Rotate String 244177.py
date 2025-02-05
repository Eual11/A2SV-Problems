# Problem: Rotate String - https://leetcode.com/problems/rotate-string/


from collections import deque
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s)!=len(goal)) :
            return False
        s_deque = deque(s)
        goal_deque = deque(goal)

        for _ in range(len(s)):
            a = s_deque.popleft()
            s_deque.append(a)
            if(goal_deque==s_deque):
                return True
        return False