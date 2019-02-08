class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if not prices:
            return 0
        
        maxProfit, pre_price = 0, prices[0]
        for price in prices[1:]:
            if price > pre_price:
                maxProfit += price - pre_price
            pre_price = price
            
        return maxProfit