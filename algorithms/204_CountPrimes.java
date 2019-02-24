class Solution {
    public int countPrimes(int n) {
        int count = 0;
        boolean[] isNotPrime = new boolean[n];
        
        for (int i=2; i<n; ++i) {
            if (!isNotPrime[i])
                ++count;
            for (int k=2*i; k<n;k+=i)
                isNotPrime[k] = true;
        }
        return count;
    }
}