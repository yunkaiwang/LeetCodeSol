class Solution:
    def searchInsert(self, nums, target):
        """
        Using Binary search, best run time 56ms beats 88%. It seems like for this question if you use linear search is faster than this binary search approach I guess it's because the test cases are all small, but if a larger array is served as one of the test case then I am sure that binary search is more efficient (tried using binary search, and best run time is 52ms beats 98%)
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        
        if left > len(nums) - 1 or nums[left] >= target:
            return left
        else:
            return left + 1