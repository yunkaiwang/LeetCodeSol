class Solution:
    def search(self, nums, target):
        """
        Potentially O(n) solution but O(logn) solution is not possible for this question
        since there are duplicate elements, so you need to linearly search through the
        elements to get rid of the duplicates otherwise you don't know which side to
        go after current step
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            while l < m and nums[m] == nums[l]:
                l += 1
            
            if nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return False