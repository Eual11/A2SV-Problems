# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X =0
        for c in operations:
            if(c == "--X" or c== "X--"):
                X-=1
            else:
                X+=1


        return X



 