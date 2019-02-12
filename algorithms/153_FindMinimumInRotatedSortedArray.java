class Solution {
    public int findMin(int[] nums) {
        if (nums.length < 1) return 0;
        int left = 0, right = nums.length - 1;
        int smallest = nums[0];
        while (left <= right){
            int mid = (int) (left + right) / 2;
            if (nums[mid] >= smallest) {
                left = mid + 1;
            } else {
                smallest = nums[mid];
                right = mid - 1;
            }
        }
        
        return smallest;
    }
}