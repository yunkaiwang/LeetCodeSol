class Solution:
    def jump(self, nums: List[int]) -> int:
        curMax, nextMax, step = 0, nums[0], 0
        for i in range(1, len(nums)):
            if i > curMax:
                curMax = nextMax
                step += 1
            nextMax = max(nextMax,i+nums[i])
        return step