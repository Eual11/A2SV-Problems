# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #God forgive me for the extra O(n) space

        tree_el =[]

        def inorder(root):
            nonlocal tree_el
            if not root:
                return
            inorder(root.left)
            tree_el.append(root)
            inorder(root.right)
        inorder(root)

        n =0

        for node in reversed(tree_el):
            v = node.val
            node.val+=n
            n+=v


        return root