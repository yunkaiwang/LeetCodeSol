class Solution {
    public int[] singleNumber(int[] nums) {
        int res = 0;
        for (int num: nums) {
            res ^= num;
        }
        
        int i = 1;
        while ((res & i) == 0) {
            i <<= 1;
        }
        int num1 = 0, num2 = 0;
        for (int num: nums) {
            if ((num & i) != 0) {
                num1 ^= num;
            } else {
                num2 ^= num;
            }
        }
        return new int[]{num1, num2};
    }
}