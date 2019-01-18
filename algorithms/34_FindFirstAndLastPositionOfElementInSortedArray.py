class Solution:
    def searchRange(self, nums, target):
        """
        Had to run binary search twice, but the runtime is still O(logn). We need to run twice since we need to find the start and end indices. Best run time 56ms beats 98%.
        """
        class Solution:
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        start, end = -1, -1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                if m > 0 and nums[m-1] == target:
                    right = m - 1
                else:
                    start = m
                    break
            elif nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        if start == -1 or nums[start] != target:
            return [-1, -1]
        left = start
        right = len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                if m < len(nums) - 1 and nums[m+1] == target:
                    left = m + 1
                else:
                    end = m
                    break
            elif nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        return [start, end]
        