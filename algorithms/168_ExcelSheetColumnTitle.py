class Solution:
    def convertToTitle(self, n: 'int') -> 'str':
        return "" if n == 0 else self.convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))