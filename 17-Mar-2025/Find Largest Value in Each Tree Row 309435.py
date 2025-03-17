# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
      Q = deque()  
      if root:
         Q.append(root)

      max_vals = []


      while Q:
        max_val = float('-inf')
        for _ in range(len(Q)):
            n = Q.popleft()
            max_val = max(max_val, n.val)
            if n.left:
                Q.append(n.left)
            if n.right:
                Q.append(n.right)
        max_vals.append(int(max_val))
      return max_vals  