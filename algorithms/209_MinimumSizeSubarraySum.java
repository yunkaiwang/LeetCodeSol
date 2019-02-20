class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int minLength = Integer.MAX_VALUE, cur_start = 0, cur_end = 0, cur_sum = 0;
        boolean found = false;
        
        while (cur_end < nums.length) {
            cur_sum += nums[cur_end];
            ++cur_end;
            while (cur_sum >= s) {
                found = true;
                minLength = Math.min(minLength, cur_end-cur_start);
                cur_sum -= nums[cur_start];
                ++cur_start;
            }
        }
        return found ? minLength : 0;
    }
}