"""
top down dp

O(m * n * L) where L is the average length of words in strs
"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for st in strs:
            numOne, numZero = st.count('0'), st.count('1')

            for i in range(m, numOne - 1, -1):
                for j in range(n, numZero - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - numOne][j - numZero] + 1)
        return dp[m][n]