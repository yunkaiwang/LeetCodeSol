class Solution {
    public int missingNumber(int[] nums) {
        int i = 0;
        while (i < nums.length) {
            if (nums[i] == i)
                i += 1;
            else {
                if (nums[i] < nums.length) {
                    int temp = nums[nums[i]];
                    if (temp == nums[i]) {
                        i += 1;
                    } else {
                        nums[nums[i]] = nums[i];
                        nums[i] = temp;
                    }
                } else {
                    i += 1;
                }
            }
        }
        
        for (i=0; i<nums.length;++i) {
            if (nums[i] != i) return i;
        }
        return i;
    }
}