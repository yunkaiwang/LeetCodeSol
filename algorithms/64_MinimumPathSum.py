class Solution:
    def minPathSum(self, grid):
        """
        same DP idea, nothing to say about this question, best run time 52ms beats 83%
        """
        n, m = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        for i in range(1, n):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        
        for i in range(1, n):
            for j in range(1, m):
                if dp[i-1][j] < dp[i][j-1]:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
        
        return dp[n-1][m-1]
        