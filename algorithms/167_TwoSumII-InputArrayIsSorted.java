class Solution {
    public int[] twoSum(int[] numbers, int target) {
        /**
         * O(n) time with O(1) space
         */
        int left = 0, right = numbers.length - 1;
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target)
                return new int[]{left+1, right+1};
            if (sum > target)
                right -= 1;
            else
                left += 1;
        }
        return new int[]{-1, -1};
    }
}