# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
       total =0 

       def helper(v, root):
        nonlocal total
        if not (root.left or root.right):
            v+=str(root.val)
            total+=int(v)
            return
        if root.left:
            helper(v+str(root.val), root.left)
        if root.right:
            helper(v+str(root.val), root.right)

       helper("", root) 

       return total