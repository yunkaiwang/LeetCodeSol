class Solution:
    def uniquePaths(self, m, n):
        """
        dynamic programming solution, best run time 32 ms beats 100%, just turns the recursive solution into two for loops to avoid many recursive calls
        """
        dp = [[0] * m] * n
        
        for i in range(m):
            dp[0][i] = 1
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[n-1][m-1]
        
        """
        Recursive solution, not so efficient, but it's still a solution
        """
        if m < 0 or n < 0:
            return 0
        elif m == 1 or n == 1:
            return 1
        elif m == 2 and n == 2:
            return 2
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)