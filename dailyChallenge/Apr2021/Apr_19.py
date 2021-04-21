class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        sol = 0
        dp = [0] * (target + 1)
        dp[0] = 1

        for t in range(1, target + 1):
            for num in nums:
                dp[t] += dp[t - num] if t >= num else 0

        return dp[-1]