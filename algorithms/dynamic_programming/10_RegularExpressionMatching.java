class Solution {
    public boolean isMatch(String s, String p) {
        boolean[][] dp = new boolean[s.length()+1][p.length()+1];
        dp[0][0] = true;
        // for cases when p string has a lot of * in the beginning, like when s = "", p = "a*b*", then this loop is useful
        for (int j=1; j<p.length(); ++j) {
            if (p.charAt(j) == '*')
                dp[0][j+1] = dp[0][j-1];
        }

        for (int i=0; i<s.length();++i) {
            char s_char = s.charAt(i);
            for (int j=0; j<p.length(); ++j) {
                // if current char is not *, then the previous string has to match, and current character has to match
                if (p.charAt(j) != '*') {
                    dp[i+1][j+1] = dp[i][j] && (s_char == p.charAt(j) || p.charAt(j) == '.');
                } else {
                    // current char is *, so there are a few cases to think about

                    // dp[i+1][j-1] represents if these two strings match without the last char + * sequence, for strings like s = "ab", p = "abc*", this will check if "ab" and "ab" match
                    // dp[i+1][j] represents if these two strings match without the *, since if so, then we can discard * for this case sicne they are already match without the *
                    // in these two cases, it's assumed that the * has no actual use, so even if they were removed, the string will still match
                    dp[i+1][j+1] |= dp[i+1][j-1] || dp[i+1][j];

                    // last case is when the * is actually in effect, the previous char in p is either . or match the current char in s, then we know that they match if they match before with the same p string, and one less character in s string
                    if (p.charAt(j-1) == '.' || p.charAt(j-1) == s_char)
                        dp[i+1][j+1] |= dp[i][j+1];
                }                
            }
        }
        
        return dp[s.length()][p.length()];
    }
}