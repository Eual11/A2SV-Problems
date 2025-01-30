# Problem: Palindrome Number  - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, s: str) -> bool:
       t = [ch.lower() for ch in s if ch.isalnum()]
       return t==t[::-1] 