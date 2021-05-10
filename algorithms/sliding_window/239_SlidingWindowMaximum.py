class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = collections.deque()
        res = [0] * (len(nums) - k + 1)

        for i in range(len(nums)):
            while arr and arr[0] < i - k + 1:
                arr.popleft()
            while arr and nums[i] >= nums[arr[-1]]:
                arr.pop()
            arr.append(i)
            if i >= k - 1:
                res[i - k + 1] = nums[arr[0]]

        return res