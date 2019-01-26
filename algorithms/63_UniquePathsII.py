class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        same DP idea, just check if there is  an obstacle, best run time 36ms beats 97%
        """
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        dp[0][0] = 1 if not obstacleGrid[0][0] else 0
        for i in range(1, m):
            if not obstacleGrid[0][i] and dp[0][i-1]:
                dp[0][i] = 1
        for i in range(1,n):
            if not obstacleGrid[i][0] and dp[i-1][0]:
                dp[i][0] = 1
            
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]
        