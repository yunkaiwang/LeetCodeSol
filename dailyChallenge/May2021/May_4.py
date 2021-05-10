class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        switched = False
        i = 0
        while i < len(nums) - 1:
            if nums[i] > nums[i+1]:
                if switched: return False
                switched = True
                if i == 0 or nums[i+1]>=nums[i-1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
            i += 1
        return True