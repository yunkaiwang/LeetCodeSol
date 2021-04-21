class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0] * 4
        for i in range(len(stoneValue)-1, -1, -1):
            dp[i%4]=-float('inf')
            take = 0
            for k in range(3):
                if i+k >= len(stoneValue):
                    break
                take += stoneValue[i+k]
                dp[i%4] = max(dp[i%4],take-dp[(i+k+1)%4])
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        return 'Tie'