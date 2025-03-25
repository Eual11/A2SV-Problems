# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
       avg_count =0 
       def solve(root):
        nonlocal avg_count
        if not root:
            return (0,0)
        ls, lc = solve(root.left)
        rs, rc = solve(root.right)
        S = root.val + ls+rs
        C =1+lc+rc

        if(S//C == root.val):
            avg_count+=1
        return (S, C)


       solve(root) 

       return avg_count