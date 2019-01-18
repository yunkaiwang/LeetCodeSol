class Solution:
    def nextPermutation(self, nums):
        """
        Have to check the solution to finally get this question, pretty interesting one, I have a similar idea but always cannot figure out some of the small problems
        """
        i = len(nums) - 2
        
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            self.swap(nums, i, j)
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    