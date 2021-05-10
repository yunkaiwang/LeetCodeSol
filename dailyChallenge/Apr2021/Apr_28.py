class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n

        dp[0] = 1 if not obstacleGrid[0][0] else 0
        for j in range(1, n):
            dp[j] = dp[j - 1] if not obstacleGrid[0][j] else 0

        for i in range(1, m):
            dp[0] = dp[0] if not obstacleGrid[i][0] else 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[j] = dp[j] + dp[j - 1]
                else:
                    dp[j] = 0

        return dp[-1]