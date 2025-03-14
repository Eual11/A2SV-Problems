# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solver(L, R):
            if L ==None and R ==None:
                return True
            elif L ==None or R ==None:
                return False
            elif R.val!=L.val:
                return False
            return solver(L.left, R.right) and solver(L.right, R.left)

        

        return solver(root.left, root.right)