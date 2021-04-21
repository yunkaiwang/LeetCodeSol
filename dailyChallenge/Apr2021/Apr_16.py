class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [(0, '?')]

        for c in s:
            if c == stack[-1][1]:
                count, _ = stack.pop()
                if count + 1 < k:
                    stack.append((count + 1, c))
            else:
                stack.append((1, c))

        return "".join([c * k for c, k in stack])