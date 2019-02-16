class Solution {
    public int trap(int[] height) {
        int sum = 0, left = 0, right = height.length - 1, left_max = 0, right_max = 0;
        
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= left_max) {
                    left_max = height[left];
                } else{
                    sum += left_max - height[left];
                }
                left += 1;
            } else {
                if (height[right] >= right_max) {
                    right_max = height[right];
                } else {
                    sum += right_max - height[right];
                }
                right -= 1;
            }
        }
        return sum;
    }
}