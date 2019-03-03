class Solution:
    def isValid(self, S: str) -> bool:
        # O(n) solution using stack
        stack = []
        for char in S:
            if char != 'c':
                stack.append(char)
            else:
                if len(stack) < 2 or stack.pop() != 'b' or stack.pop() != 'a':
                    return False
        return len(stack) == 0

        # O(n^n) solution, recursively remove 'abc' until the string is empty or 'abc' doesn't exist in string any more
        if S == 'abc':
            return True
        index = S.find('abc')
        if index == -1:
            return False
        return self.isValid(S[:index]+S[index+3:])