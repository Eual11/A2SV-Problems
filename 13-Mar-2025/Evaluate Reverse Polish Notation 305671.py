# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oprand_stack = []
        for tk in tokens:
            if(tk not in "+-*/"):
                oprand_stack.append(int(tk))
            else:
                #evaluating 
                if(tk =="+"):
                    if(len(oprand_stack)>=2):
                        op2 = oprand_stack.pop()
                        op1 = oprand_stack.pop()
                        oprand_stack.append(op1+op2)
                elif(tk == '-'):
                    if(len(oprand_stack)>=2):
                        op2 = oprand_stack.pop()
                        op1 = oprand_stack.pop()
                        oprand_stack.append(op1-op2)
                elif(tk=='*'):
                    if(len(oprand_stack)>=2):
                        op2 = oprand_stack.pop()
                        op1 = oprand_stack.pop()
                        oprand_stack.append(int(op1*op2))
                elif(tk=='/'):
                    if(len(oprand_stack)>=2):
                        op2 = oprand_stack.pop()
                        op1 = oprand_stack.pop()
                        oprand_stack.append(int(op1/op2))

        return int(oprand_stack.pop());
