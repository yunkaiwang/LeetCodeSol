class Solution:
    def maxSubArray(self, nums):
        """
        Very simple question, we add current number to the sum if it creates a larger sum,
        if not, then the new sum contains only current number itself, so we only need O(n)
        time and O(1) space, beats 100% on LeetCode.

        Divide and conquer (as described in the description) is also possible for this question,
        the only thing we need to care about when we use divide and conquer is that when we merge,
        is possible that there exist a better solution containing the last few numbers from the
        left and the first few numbers from the right, so we need to do a check there, the overall
        run time will be O(n logn) using divide and conquer
        """
        max, max_so_far = -float('inf'), 0
        for num in nums:
            if max_so_far + num < num:
                max_so_far = num
            else:
                max_so_far = max_so_far + num
            
            if max_so_far > max:
                max = max_so_far
        return max
        