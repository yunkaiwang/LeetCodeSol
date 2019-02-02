class Solution:
    def grayCode(self, n):
        sol = []
        for i in range(1 << n):
            sol.append((i >> 1) ^ i)
        return sol