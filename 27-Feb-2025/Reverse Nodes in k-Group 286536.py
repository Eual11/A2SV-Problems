# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        def reverse(np, h):

            if(not h.next or not h):
                return h
            head = h 
            prev = np 

            while(head!=np):
                nextNode = head.next
                head.next = prev 
                prev = head
                head =  nextNode
            return prev

        prevHead = None
        start = head

        while(start):
            i = 0 
            end = start
            while(end and i < k):
                end = end.next
                i+=1
            hd = start
            if(i ==k):
                if(prevHead):
                    prevHead.next = reverse(end, start)
                else:
                    head = (reverse(end, start))
                prevHead = hd
            start = end
        return head

