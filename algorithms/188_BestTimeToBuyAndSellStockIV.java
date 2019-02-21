class Solution {
    public int maxProfit(int k, int[] prices) {
        if (k >= prices.length / 2) {
            int profit = 0;
            for (int i=1; i<prices.length; ++i) {
                profit += Math.max(prices[i]-prices[i-1], 0);
            }
            return profit;
        }
        
        int[] states = new int[k * 2 + 1];
        for (int i=1; i< states.length; i+=2) {
            states[i] = Integer.MIN_VALUE;
        }
        for (int price: prices) {
            for (int i = states.length - 1; i > 0; --i) {
                if (i % 2 != 0) {
                    states[i] = Math.max(states[i], states[i-1] - price);
                } else {
                    states[i] = Math.max(states[i], states[i-1] + price);
                }
            }
        }
        int max = states[0];
        for (int i=2; i<states.length; i+=2) {
            if (states[i] > max)
                max = states[i];
        }
        return max;
    }
}