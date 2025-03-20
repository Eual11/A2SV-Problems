# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root, curMin, curMax):

            if not root:
                return abs(curMin-curMax)
            
            curMin = min(root.val, curMin)
            curMax = max(root.val, curMax)

            L_diff = helper(root.left, curMin, curMax)
            R_diff = helper(root.right, curMin, curMax)

            return max(L_diff, R_diff)
        return helper(root, root.val, root.val)
