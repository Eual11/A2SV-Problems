# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:


        n = len(names)

        #selection sort
        for i in range(n):
            max_idx = i

            for j in range(i+1, n):

                if(heights[j] > heights[max_idx]):
                    max_idx = j
            if(max_idx!=i):
                heights[max_idx], heights[i] = heights[i], heights[max_idx]
                names[max_idx], names[i] = names[i],names[max_idx]
        return names

    
                
