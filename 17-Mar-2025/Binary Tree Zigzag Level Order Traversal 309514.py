# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       Q = deque() 

       if root:
        Q.append(root)

       levels =[]

       lev =0

       while Q:
        l_arr =[]
        for _ in range(len(Q)):
            n = Q.popleft()
            if n.left:
                Q.append(n.left)
            if n.right:
                Q.append(n.right)
            l_arr.append(n.val)
        if lev%2==1:
            l_arr.reverse()
        levels.append(l_arr)
        lev+=1



       return levels