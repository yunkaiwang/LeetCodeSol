class Solution {
    public int maxProduct(int[] nums) {
        int max = Integer.MIN_VALUE;
        int curProduct = 1;
        for (int num: nums) {
            curProduct *= num;
            if (curProduct > max)
                max = curProduct;
            
            if (num == 0)
                curProduct = 1;
        }
        curProduct = 1;
        for (int i=nums.length-1;i>-1;--i){
            curProduct *= nums[i];
            if (curProduct > max)
                max = curProduct;
            if (nums[i] == 0)
                curProduct = 1;
        }
        return max;
    }
}