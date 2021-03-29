class Solution:
    def search(self, nums, target):
        """
        Modified binary search without finding the rotating index,
        best runtime 56ms beats 99%

        This idea is that when we get rid of half of the elements,
        we need to make sure if the half is sorted or not, if it's
        not sorted, then we need to further check the elements to see
        if the target will fall in this half or not
        """
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1