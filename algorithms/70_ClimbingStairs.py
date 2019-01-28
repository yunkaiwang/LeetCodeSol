class Solution:
    def climbStairs(self, n):
        """
        very easy question, simply DP or recursive will do the job in O(n) time with O(n) space, the recursive one is also correct will will exceeed time limit, but it's still a solution. Runs in 32ms beats 100%
        """
        if n < 2:
            return 1
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
        
        
        """recursive solution"""
        if n < 1:
            return 0
        elif n < 2:
            return 1
        elif n < 3:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)