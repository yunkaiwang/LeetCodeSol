class Solution:
    def sortColors(self, nums):
        """
        idea based on bucket sort, use constant extra space and linear time. r, w, b represents the last index of the three colors so that when we have a new color, we can use those three variables to know which elements we need to shift in order to keep array sorted
        """
        r, w, b = 0, 0, 0
        for i, num in enumerate(nums):
            if num == 2:
                b += 1
            elif num == 1:
                nums[i] = nums[w]
                nums[w] = 1
                w += 1
                b += 1
            elif num == 0:
                nums[i] = nums[w]
                nums[w] = nums[r]
                nums[r] = 0
                r += 1
                w += 1
                b += 1