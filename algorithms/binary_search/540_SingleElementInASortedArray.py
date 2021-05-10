# given an array of n sorted integers, exactly one integer in the list appeared exactly once
# find the integer that appeared once

# [1,1,2,2,3,4,4] -> 3

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
            # if not arr or len(arr)%2 == 0: return -1
            #
            # # arr has at least 3 numbers
            # left, right = 0, len(arr) - 1
            # while left < right:
            #     mid = left + (right-left)//2
            #     if mid % 2 == 0:
            #         if arr[mid] == arr[mid+1]:
            #             left=mid+2
            #         else:
            #             right=mid
            #     else:
            #         if arr[mid] == arr[mid-1]:
            #             left=mid+1
            #         else:
            #             right=mid-1
            #
            # return arr[left]