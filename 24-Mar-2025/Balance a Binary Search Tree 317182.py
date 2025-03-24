# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

      tree_arr =[]
      def inorder(root):
        if not root:
            return
        inorder(root.left)
        tree_arr.append(root.val)
        inorder(root.right)

      inorder(root)

      def createTree(l, r):
        if l >r:
            return None
        m = l+((r-l)//2)
        root = TreeNode(tree_arr[m])
        root.left = createTree(l, m-1)
        root.right = createTree(m+1, r)
        return root

      return createTree(0, len(tree_arr)-1)  



      return root