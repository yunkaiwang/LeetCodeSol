class Solution {
    public int findMin(int[] nums) {
        if (nums.length < 1) return 0;
        int left = 0, right = nums.length - 1;
        while (left < right){
            int mid = (left + right) / 2;
            
            if (nums[right] < nums[mid]) {
                left = mid + 1;
            } else if (nums[mid] < nums[right]) {
                right = mid;
            } else {
                if (nums[left] == nums[mid]) {
                    ++left;
                    --right;
                } else {
                    right = mid;
                }
            }
        }
        
        return nums[right];
    }
}