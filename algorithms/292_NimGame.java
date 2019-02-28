class Solution {
    public boolean canWinNim(int n) {
        /**
         * Dynamic programming solution using O(n) time and O(1) space
         */
        if (n < 4) return true;
        boolean a = true, b = true, c = true;
        for (int i=3;i<n;++i) {
            boolean d = !a || !b || !c;
            a = b;
            b = c;
            c = d;
        }
        return c;
    }
}