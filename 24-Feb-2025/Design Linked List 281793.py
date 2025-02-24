# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:

    def __init__(self, val, prev=None, next =None):
        self.val = val
        self.prev = prev
        self.next = next
class MyLinkedList:
    

    def __init__(self):
        self.head = None
        self.tail = None
        self.len =0
        

    def get(self, index: int) -> int:

        if not self.head or index >= self.len:
            return -1
        cur = self.head

        while index >0:
            cur = cur.next
            index-=1
        return cur.val


        
        

    def addAtHead(self, val: int) -> None:
        if not (self.head or self.tail):
            self.head = self.tail = Node(val)
        else:
            new_node = Node(val, None, self.head)

            self.head.prev = new_node

            self.head = new_node
        self.len+=1

    def addAtTail(self, val: int) -> None:
        if not (self.head or self.tail):
            self.head = self.tail = Node(val)
        else:
            new_node = Node(val, self.tail, None)
            self.tail.next = new_node
            self.tail = new_node
        self.len+=1
        

    def addAtIndex(self, index: int, val: int) -> None:

        cur = self.head

        if index == self.len:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index > self.len:
            return

        while cur and index >0:
            cur = cur.next
            index-=1
       
        prev = cur.prev
        new_node = Node(val, prev, cur)
        prev.next = new_node
        cur.prev = new_node
        self.len+=1
        

    def deleteAtIndex(self, index: int) -> None:
 
        cur = self.head
        if index >=self.len:
            return
        if self.len==1:
            self.head = self.tail = None
            self.len-=1
            return

        if index == self.len-1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            self.len-=1
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.len-=1
            return

        while cur and index >0:
            cur = cur.next
            index-=1
       
        prev = cur.prev
        next = cur.next
        if prev:
            prev.next = cur.next
        if next:
            next.prev = prev
        self.len-=1

       


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)