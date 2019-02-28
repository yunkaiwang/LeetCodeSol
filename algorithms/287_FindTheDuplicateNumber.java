class Solution {
    public int findDuplicate(int[] nums) {
        /**
         * If we are allowed to change the input array, then we can simple move all numbers to their correct position, and as soon as we find one element whose position has been ocupied, we can return that element since that will be the duplicate element. Runtime will be O(n) and space complexity will be O(1)
         * 
         * If we can use O(n) memory, then we can simple set up a hashset, and as soon as we find an element that has appeared in the hashset, we return that element, and runtime will be O(n) and space complexity will be O(1).
         * 
         * The solution described below runs in O(n logn) time, the idea is based on binary search, and every time we count the number elements between [left, mid] range, whenever the number of elements in this range exceed the size of the range, we know that the duplicate element will be in this range, otherwise, we go right.
         */
        int left = 1, right = nums.length-1;
        while (left < right) {
            int leftC = 0, rightC = 0;
            int mid = left + ((right - left) >> 1);
            for (int num: nums) {
                if (num < left || num > right)
                    continue;
                if (num <= mid)
                    ++leftC;
                else
                    ++rightC;
            }
            
            if ((left == mid && leftC > 1) || leftC > mid - left + 1)
                right = mid;
            else
                left = mid + 1;
            
        }
        return left;
    }

    /**
     * Great idea using O(n) time and O(1) space based on detecting cycle in cyclic linked list, but it's too hard to think of during real interview
     */
    public int findDuplicate2(int[] nums) {
        int p1 = 0, p2 = 0;
        do {
            p1 = nums[p1];
            p2 = nums[nums[p2]];
        } while (p1 != p2);
        p2 = 0;
        while (p1 != p2) {
            p1 = nums[p1];
            p2 = nums[p2];
        }
        return p1;
    }
}