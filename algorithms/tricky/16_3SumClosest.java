class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int closest = Integer.MAX_VALUE;
        
        Arrays.sort(nums); // nlog(n)
        
        // n^2
        for (int i = 0; i < nums.length - 2; ++i) {
            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int cur_sum = nums[i] + nums[left] + nums[right];
                if (cur_sum == target) return target;
                if (Math.abs(target - cur_sum) < Math.abs(target - closest) || closest == Integer.MAX_VALUE)
                    closest = cur_sum;
                
                if (cur_sum > target)
                    right -= 1;
                else
                    left += 1;
            }
        }
        return closest;
    }
}