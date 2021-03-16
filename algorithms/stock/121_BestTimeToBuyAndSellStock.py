class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if not prices:
            return 0
        maxProfit = 0
        cur_lowest_price = prices[0]
        for price in prices[1:]:
            if price < cur_lowest_price:
                cur_lowest_price = price
            else:
                maxProfit = max(maxProfit, price - cur_lowest_price)
        return maxProfit