class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1
        while left<right:
            mid = (right-left)//2+left
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        if not nums or nums[right] != target:
            return [-1,-1]
        first = right
        left,right=right,len(nums)-1
        while left<right:
            mid = (right-left)//2+left
            if nums[mid]>target:
                right=mid
            else:
                left=mid+1
        return [first,right-1] if nums[right] != target else [first,right]