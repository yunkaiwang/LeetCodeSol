"""
Palindromic Substrings

O(n^2) solution, expanding every possible center.
Can be simplified to O(n) time solution by using
Manacher's Algorithm.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def checkPalindrome(left, right):
            count = 0
            while left > -1 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(len(s)):
            count += checkPalindrome(i, i + 1)
            count += checkPalindrome(i, i)
        return count