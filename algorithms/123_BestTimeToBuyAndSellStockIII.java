class Solution {
    public int maxProfit(int[] prices) {
        int[] states = new int[5];
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