"""
Reordered Power of 2

O(log(n)!) time solution, check each possible permutation
is a power of 2 or not
"""
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        if N < 1: return False

        digits = []
        while N:
            digits.append(N % 10)
            N //= 10

        def combination(l_digits, c_num):
            if len(l_digits) == 0:
                if self.isPowerOf2(c_num):
                    return True
            else:
                for i in range(len(l_digits)):
                    if combination(l_digits[:i] + l_digits[1 + i:], c_num * 10 + l_digits[i]):
                        return True
                return False

        for i in range(len(digits)):
            if digits[i] != 0:
                if combination(digits[:i] + digits[i + 1:], digits[i]):
                    return True
        return False

    def isPowerOf2(self, N: int) -> bool:
        return N & (N - 1) == 0