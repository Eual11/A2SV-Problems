# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
       Q = deque([root])


       level =0


       while Q:
        level_size = len(Q) 
        nodes = list(Q)


        if level%2:
            l = 0
            r =len(nodes)-1

            while l <r:
                nodes[l].val, nodes[r].val = nodes[r].val, nodes[l].val
                l+=1
                r-=1

        for _ in range(level_size):
            n = Q.popleft()

            if n.left:
                Q.append(n.left)
            if n.right:
                Q.append(n.right)
        level+=1

       return root
        