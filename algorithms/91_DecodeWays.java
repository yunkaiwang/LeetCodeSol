class Solution {
    public int numDecodings(String s) {
        if (s == null || s.charAt(0) == '0') {
            return 0;
        }
        int a = 1, b = 1, i = 1, c;
        while (i < s.length()) {
            if (s.charAt(i) < '1') {
                if (s.charAt(i-1) > '2' || s.charAt(i-1) < '1') {
                    return 0;
                } else {
                    c = a;
                }
            } else if (s.charAt(i-1) > '0' && s.substring(i-1, i + 1).compareTo("27") < 0) {
                c = a + b;
            } else {
                c = b;
            }
            i += 1;
            a = b;
            b = c;
        }
        return b;
    }
}