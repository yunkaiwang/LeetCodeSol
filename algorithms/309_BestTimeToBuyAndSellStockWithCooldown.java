class Solution {
    public int maxProfit(int[] prices) {
        /**
         * exponential algorithm, will get a TLE error on leetcode
         */
        if (prices.length < 2) {
            return 0;
        }
        return helper(-1, prices, 0);
    }
    
    public int helper(int currentPrice, int[] prices, int index) {
        if (index > prices.length - 2) {
            if (currentPrice == -1) {
                return 0;
            } else {
                return currentPrice < prices[index] ? prices[index] - currentPrice : 0;
            }
        }
        
        if (currentPrice == -1) {
            int x = helper(prices[index], prices, index+1);
            int y = helper(-1, prices, index+1);
            return Math.max(x, y);
        } else {
            if (prices[index] > currentPrice) {
                return Math.max(prices[index]-currentPrice+helper(-1, prices, index+2), helper(currentPrice, prices, index+1));
            } else {
                return helper(currentPrice, prices, index+1);
            }
        }
    }
}