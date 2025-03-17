# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

       if not root:
        return TreeNode(val) 
       prev = root
       next = root

       while next:
        if next.val <= val:
            prev = next
            next = next.right
        else:
            prev = next
            next = next.left

       if prev.val <=val:
        prev.right = TreeNode(val) 
       else:
        prev.left = TreeNode(val)    

       return root 