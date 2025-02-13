# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        left, right = 0, len(people)-1
        people.sort()

        cnt =0
        while (left < right):
            if(people[left]+people[right] <= limit):
                left+=1
                right-=1
            else:
                right-=1
            cnt+=1
        if(left==right):
            cnt+=1
        return cnt
        
