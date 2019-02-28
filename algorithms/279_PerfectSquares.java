class Solution {
    public int numSquares(int n) {
        /**
         * O(n * sqrt(n)) solution using dynamic programming, beats 30%
         * Not using mathematical solution since those are almost impossible to think of during actaul interview
         */
        int[] dp = new int[n];
        Arrays.fill(dp, Integer.MAX_VALUE);
        for (int i=1; i<Math.ceil(Math.sqrt(n+1)); ++i) {
            dp[(int)Math.pow(i, 2)-1] = 1;
        }
        
        for (int i=1; i<n; ++i) {
            for (int j=1; j<Math.ceil(Math.sqrt(i+1)); ++j)
                dp[i] = Math.min(dp[i], 1+dp[i-(int)Math.pow(j, 2)]);
        }
        return dp[n-1];
    }
}