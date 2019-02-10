class Solution(object):
    def numDistinct(self, s, t):
        dp = [1] + [0 for _ in t]
        for c in s:
            for i, match_c in enumerate(t[::-1]):
                if c == match_c:
                    dp[len(t) - i] += dp[len(t) - i - 1]
                    
        return dp[-1]