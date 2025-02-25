# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        merged =[]

        l = r = 0

        while l < len(firstList) and r < len(secondList):

            A = firstList[l]
            B = secondList[r]

            if max(A[0], B[0]) <=min(A[1],B[1]):
                merged.append([max(A[0], B[0]), min(A[1],B[1])])
            if A[1] <B[1]:
                l+=1
            else:
                r+=1




        return merged