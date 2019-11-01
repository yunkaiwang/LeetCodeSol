class Solution:
    def removeDuplicates(self, nums):
        # O(n) solution is obvious, nothing to say about this question
        if not nums: return 0
        
        count = 1
        for i, num in enumerate(nums):
            if num != nums[count-1]:
                nums[count] = num
                count += 1
        return count