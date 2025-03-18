# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       def bst(root, val):
        if not root:
            return False
        if root.val == val:
            return True
        if root.val > val:
            return bst(root.left, val)
        if root.val < val:
            return bst(root.right, val)

       LCA = root

       def solver(root, a, b):
            nonlocal LCA
            if not root:
                return
            if bst(root, a.val) and bst(root,b.val):
                LCA = root
                solver(root.left, a, b)
                solver(root.right, a,b) 
       solver(root, p, q)
       return LCA