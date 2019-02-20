class Solution:
    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums) - 1)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start] = nums[start] + nums[end]
            nums[end] = nums[start] - nums[end]
            nums[start] = nums[start] - nums[end]
            start += 1
            end -= 1