"""
Longest valid parentheses

Two pass with constant extra space
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest, cur, start = 0, 0, -1
        i = 0
        while i < len(s):
            if s[i] == "(":
                cur += 1
            else:
                cur -= 1
                if cur == 0:
                    longest = max(longest, i-start)
                elif cur < 0:
                    cur, start = 0, i
            i += 1
        cur, end = 0, len(s)
        i = len(s) - 1
        while i > -1:
            if s[i] == ")":
                cur += 1
            else:
                cur -= 1
                if cur == 0:
                    longest = max(longest, end - i)
                elif cur < 0:
                    cur, end = 0, i
            i -= 1
        return longest