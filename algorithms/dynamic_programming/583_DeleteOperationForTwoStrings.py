class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [0] * (n+1)
        for j in range(n+1):
            dp[j] = j
        for i in range(1,m+1):
            cross = dp[0]
            dp[0] = i
            for j in range(1,n+1):
                prev = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = cross
                else:
                    dp[j] = 1 + min(dp[j],dp[j-1])
                cross = prev
        return dp[-1]