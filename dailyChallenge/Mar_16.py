"""
Best Time to Buy and Sell Stock with Transaction Fee

Description: You are given an array prices where prices[i]
is the price of a given stock on the ith day, and an integer
fee representing a transaction fee. Find the maximum profit
you can achieve. You may complete as many transactions as you
like, but you need to pay the transaction fee for each transaction.

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Solution: Simple O(n) solution based on dp
cash - the max profit if we don't process any stock on day k
hold - the max profit if we process a stock on day k
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash
