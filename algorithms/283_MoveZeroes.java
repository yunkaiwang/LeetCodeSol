class Solution {
    public void moveZeroes(int[] nums) {
        int curIndex = 0, firstIndex = 0;
        while (curIndex < nums.length) {
            if (nums[curIndex] == 0)
                ++curIndex;
            else {
                nums[firstIndex] = nums[curIndex];
                if (firstIndex != curIndex)
                    nums[curIndex] = 0;
                ++firstIndex;
                ++curIndex;
            }
        }
    }
}