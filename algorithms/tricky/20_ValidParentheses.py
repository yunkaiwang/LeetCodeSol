class Solution:
    def isValid(self, s):
        stack = []
        match = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in ["{", "(", "["]:
                stack.extend(char)
            else:
                if not stack or match[stack[-1]] != char:
                    return False
                stack.pop()
        return len(stack) == 0