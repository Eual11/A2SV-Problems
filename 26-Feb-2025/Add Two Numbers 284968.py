# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(1) 

        rem =0
        prev =dummy

        while l1 or l2:
            a =b =0
            if l1:
                a = l1.val
            if l2:
                b = l2.val
            c = a+b+rem
            rem = c//10
            c = c%10
            prev.next = ListNode(c)
            prev = prev.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if rem:
            prev.next = ListNode(rem)
        return dummy.next