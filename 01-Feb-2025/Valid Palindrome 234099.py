# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
       t = [ch.lower() for ch in s if ch.isalnum()]
       return t==t[::-1] 