class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0) return new int[0];
        Deque<Integer> deq = new LinkedList<Integer>();
        int[] res = new int[nums.length - k + 1];
        for (int i=0; i<k; ++i) {
            while (!deq.isEmpty() && nums[i] >= nums[deq.peekLast()])
                deq.removeLast();
            deq.addLast(i);
        }
        for (int i=k; i<nums.length; ++i) {
            res[i-k] = nums[deq.peekFirst()];
            while (!deq.isEmpty() && deq.peekFirst() <= i-k)
                deq.removeFirst();
            while (!deq.isEmpty() && nums[i] >= nums[deq.peekLast()])
                deq.removeLast();
            deq.addLast(i);
        }
        res[nums.length-k] = nums[deq.peekFirst()];
        return res;
    }
}