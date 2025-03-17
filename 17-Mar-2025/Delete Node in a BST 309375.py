# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def findMin(node):
            if not node:
                return node
            while node.left:
                node = node.left
            return node

        def helper(root, val):

            if not root:
                return root
            if root.val < val:
                root.right = helper(root.right, val)
            elif root.val > val:
                root.left = helper(root.left, val)
            else:
                # has only one or less node
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left

                #has two children, so we remove the inorder sucessor

                temp = findMin(root.right)
                root.val = temp.val

                root.right = helper(root.right, temp.val)


            return root




            
                



        return helper(root, key)
        