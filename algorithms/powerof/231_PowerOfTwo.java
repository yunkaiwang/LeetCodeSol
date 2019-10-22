class Solution {
    public boolean isPowerOfTwo(int n) {
        /**
         * O(1) solution, if n is a power of 2, then in binary, n is 100...0 (assume there are k 0s), then n-1 is 111...1 (k 1s)
         * then n&(n-1) = 0, if not, then the result will be something else
         */
        if (n < 1)
            return false;
        return (n&(n-1)) == 0;
    }

    public boolean isPowerOfTwo(int n) {
        /**
         * O(logn) solution
         */
        while (n > 1) {
            if ((n & 1) == 1)
                return false;
            n >>= 1;
        }
        return n == 1 ? true : false;
    }
}