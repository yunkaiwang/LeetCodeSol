class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[0, '?']]

        for c in s:
            if c == stack[-1][1]:
                stack[-1][0] += 1
                if stack[-1][0] == k:
                    stack.pop()
            else:
                stack.append([1, c])

        return "".join(c * k for c, k in stack)