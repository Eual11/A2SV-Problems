# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        chem = 0
        skill.sort()

        prev =0

        l =0
        r = len(skill)-1

        while(l <r):

            if(prev !=0 and prev != skill[l]+skill[r]):
                return -1
            elif prev ==0:
                prev = skill[l]+skill[r]
            chem+=skill[l]*skill[r]

            l+=1
            r-=1




        return chem        
