"""
Wiggle Subsequence

Description: Given an integer array nums, return the length of the longest wiggle sequence.

Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.

Solution: O(n) solution with constant space

If the current number is larger than the previous one, then
we can add one to the longest sequence that was going down.
When the current number is smaller than the previous one, then
we can add one to the longest sequence that was going up.
"""
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return len(nums)

        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)