# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(names)


        for i in range(1, n):
            key = heights[i]
            key_name = names[i]
            j = i-1

            while j >=0 and heights[j] < key:
                heights[j+1] = heights[j]
                names[j+1] = names[j]

                j-=1
            heights[j+1] = key
            names[j+1] = key_name

        return names

        

        
 