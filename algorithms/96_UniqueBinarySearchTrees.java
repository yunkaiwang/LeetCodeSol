class Solution {
    public int numTrees(int n) {
        if (n == 0) { return 0; }
        
        int[] arr = new int[n];
        for (int i=0; i<n;++i) {
            arr[i] = 0;
        }
        return dfs(n, arr);
    }
    
    public int dfs(int n, int[] arr) {
        if (n == 0) {
            return 1;
        } else if (arr[n-1] != 0) {
            return arr[n-1];
        }
        int total = 0;
        for (int i=0; i<n; ++i) {
            int left_count = dfs(i, arr);
            int right_count = dfs(n-i-1, arr);
            total += left_count * right_count;
        }
        arr[n-1] = total;
        return total;
    }
}