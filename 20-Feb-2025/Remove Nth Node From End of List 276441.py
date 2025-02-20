# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = 0

        #first scan to determine list length
        tmp = head
        while(tmp):
            list_len+=1
            tmp = tmp.next
        if(list_len <=1):
            return None
        idx =0
        pos = list_len-n-1
        if(pos <0):
            return head.next
        tmp = head
        while(tmp):
            if(idx ==pos):
                tmp.next = tmp.next.next
            idx+=1
            tmp = tmp.next
        return head