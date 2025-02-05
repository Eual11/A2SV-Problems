# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
        def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
                index_dict = {}
                for i, val in enumerate(list1):
                        index_dict[val] = i
                res =[]
                min_val = float('inf')
                for i, val in enumerate(list2):
                    if(val in index_dict):
                            idx = i+index_dict[val]

                            if(idx < min_val):
                                    res = [val]
                                    min_val = idx
                            elif(idx == min_val):
                                    res.append(val)    
                return res
 