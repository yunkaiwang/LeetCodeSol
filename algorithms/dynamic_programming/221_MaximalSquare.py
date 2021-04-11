"""
O(mn) solution with O(n) space,
can be improved to O(min(m,n)) space
if we transpose the matrix when n>m
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)

        maxSquare = 0
        for i in range(m):
            prev = 0
            for j in range(n):
                if matrix[i][j] == "1":
                    temp = dp[j + 1]
                    dp[j + 1] = 1 + min(dp[j], dp[j + 1], prev)
                    prev = temp
                    maxSquare = max(maxSquare, dp[j + 1] * dp[j + 1])
                else:
                    prev = dp[j + 1]
                    dp[j + 1] = 0

        return maxSquare