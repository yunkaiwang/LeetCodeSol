class Solution {
    public int minDistance(String word1, String word2) {
        int l1 = word1.length();
        int l2 = word2.length();
        int[][] dp = new int[l1+1][l2+1];
        for (int i=1; i<l1+1;++i){
            dp[i][0] = i;
        }
        for (int i=1; i<l2+1;++i){
            dp[0][i] = i;
        }
        
        for (int i=1; i<l1+1; ++i) {
            for (int j = 1; j<l2+1; ++j) {
                /**
                 * If current char of word1 and word2 match, then dp[i][j] simply equals to dp[i-1][j-1], if they don't match
                 * suppose current char of word1 is c, current char of word2 is d, there are three options how we can change
                 * word1[:i] to word2[:j]
                 * 
                 * 1. We replace c with d, so dp[i][j] = dp[i-1][j-1]+1
                 * 2. We add d to the end, so dp[i][j] = dp[i][j-1]+1
                 * 3. We delete c from the end, so dp[i][j] = dp[i-1][j]+1
                 * 
                 * Then we can simply use the minimum of these 3 as the dp[i][j] value
                 */
                int cross = dp[i-1][j-1];
                if (word1.charAt(i-1) != word2.charAt(j-1))
                    ++cross;
                
                int delete = dp[i-1][j] + 1;
                int add = dp[i][j-1] + 1;
                int min = Math.min(add, delete);
                min = Math.min(min, cross);
                dp[i][j] = min;
            }
        }
        return dp[l1][l2];
    }
}