"""
Coin Change

Description: You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Solution: Use dynamic programming for this problem
Time: O(amount * |coins|)
Space: O(amount)
We find what is the smallest number of coins (s) possible to make a k amount return, then
the smallest number to make a coin[i]+k amount return is clearly 1+s.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        if len(coins) == 1:
            return -1 if amount % coins[0] else amount / coins[0]
        elif amount == 0:
            return 0

        coins.sort()

        if coins[0] == 1:
            dp = [i for i in range(amount + 1)]
        else:
            dp = [-1 for _ in range(amount + 1)]

        for coin in coins:
            index = 1
            while coin * index <= amount:
                dp[coin * index] = index
                index += 1

        for i in range(amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] != -1:
                    if dp[i] == -1:
                        dp[i] = 1 + dp[i - coin]
                    else:
                        dp[i] = min(1 + dp[i - coin], dp[i])
        return dp[-1]