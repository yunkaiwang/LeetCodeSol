"""
O(n^2) solution with O(n) space based on dynamic programming
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max(i - j, dp[i - j]) * max(j, dp[j]))

        return dp[-1]