class Solution {
    public int[] productExceptSelf(int[] nums) {
        /**
         * O(n) solution without using division and use constant extra space
         */
        int[] res = new int[nums.length];
        res[0] = 1;
        for (int i=1; i<nums.length; ++i)
            res[i] = res[i-1] * nums[i-1];
        
        int right = 1;
        for (int i=nums.length-2;i>-1;--i) {
            right *= nums[i+1];
            res[i] *= right;
        }
            
        return res;
    }

    public int[] productExceptSelf(int[] nums) {
        /**
         * O(n) solution using division and constant extra space
         */
        int product = 1, zeroCount = 0;
        for (int num : nums) {
            if (num != 0)
                product *= num;
            else
                ++zeroCount;
        }
            
        
        int[] res = new int[nums.length];
        for (int i=0;i<nums.length;++i) {
            if (zeroCount > 1)
                res[i] = 0;
            else if (zeroCount == 1) {
                if (nums[i] == 0)
                    res[i] = product;
                else
                    res[i] = 0;
            } else
                res[i] = product / nums[i];
        }
            
        return res;
    }
}