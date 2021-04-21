class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack=["?"]
        for c in S:
            if c==stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack[1:])