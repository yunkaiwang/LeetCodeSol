"""
Solution based on KMP algorithm
"""
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        elif not A:
            return True
        newA = A + A[:-1]
        p = [0] * len(B)
        for i in range(1, len(B)):
            l = p[i - 1]
            while l > 0 and B[l] != B[i]:
                l = p[l - 1]

            if B[l] == B[i]:
                l += 1
            p[i] = l

        i, j = 0, 0
        while i < len(newA):
            if newA[i] == B[j]:
                i += 1
                j += 1
            if j == len(B):
                return True
            elif i < len(newA) and B[j] != newA[i]:
                if j != 0:
                    j = p[j - 1]
                else:
                    i += 1

        return False