# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # getting length of the list

        temp = head
        n =0

        while temp:
            n+=1
            temp = temp.next
        m = (n+1)//2

        print("test")
        aheadNode = head

        while m >0:
            aheadNode = aheadNode.next
            m-=1
        while aheadNode:
            head = head.next
            aheadNode = aheadNode.next

        return head


