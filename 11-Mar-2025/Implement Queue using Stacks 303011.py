# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue(object):

    def __init__(self):

        self.pop_stk =[]
        self.push_stk =[]
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.push_stk.append(x)
        

    def pop(self):
        """
        :rtype: int
        """

        if self.pop_stk !=[]:
            return self.pop_stk.pop()
        else:
            while len(self.push_stk) !=1:
                self.pop_stk.append(self.push_stk.pop())
            
            t = self.push_stk.pop()
            return t
        

    def peek(self):
        """
        :rtype: int
        """

        if self.pop_stk !=[]:
            return self.pop_stk[-1]
        else:
            while self.push_stk!=[]:
                self.pop_stk.append(self.push_stk.pop())
            return self.pop_stk[-1]


        

    def empty(self):
        """
        :rtype: bool
        """
        return self.pop_stk ==[] and self.push_stk==[]
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()