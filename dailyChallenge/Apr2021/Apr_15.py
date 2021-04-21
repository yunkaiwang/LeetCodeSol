class Solution:
    def fib(self, n: int) -> int:
        if n < 2: return n
        dp1, dp2 = 0, 1
        for i in range(1, n):
            dp1, dp2 = dp2, dp1 + dp2
        return dp2