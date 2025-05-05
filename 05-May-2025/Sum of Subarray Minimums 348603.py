# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        stack = []
        prev_less = [None] * n
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []
        next_less = [None] * n
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_less[i] = stack[-1] if stack else n
            stack.append(i)
        
        result = 0
        for i in range(n):
            left = i - prev_less[i]
            right = next_less[i] - i
            result += arr[i] * left * right
            result %= MOD
        
        return result
