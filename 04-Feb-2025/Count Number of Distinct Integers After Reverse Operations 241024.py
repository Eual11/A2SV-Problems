# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
       uniq =set()

       for n in nums: 
            uniq.add(n)
            uniq.add(int(str(n)[::-1]))

       return len(uniq) 