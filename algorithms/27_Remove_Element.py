class Solution:
    def removeElement(self, nums, val):
        """
        O(n) solution, very similar to question 26, nothing to say about this
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count