class Solution {
    public int lengthOfLIS2(int[] nums) {
        /**
         * O(n logn) time using Binary search
         */
        int[] dp = new int[nums.length];
        
        int size = 0;
        for (int i=0;i<nums.length;++i) {
            int left = 0, right = size;
            while (left < right) {
                int mid = left + ((right-left)>>1);
                if (nums[i] <= dp[mid])
                    right = mid;
                else
                    left = mid + 1;
            }
            dp[left] = nums[i];
            if (left == size)
                ++size;
            
        }
        
        return size;
    }

    public int lengthOfLIS(int[] nums) {
        /**
         * O(n^2) solution
         */
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        int max = 0;
        for (int i=0;i<nums.length;++i) {
            for (int j=0;j<i;++j) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], 1+dp[j]);
                }
            }
            max = Math.max(dp[i], max);
        }
        return max;
    }
}