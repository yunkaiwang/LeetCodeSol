"""
Beautiful arrangement II

O(n) solution with O(n) space

Runtime is slow on LeetCode compared to other solutions,
maybe because of the function call stack?
"""
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        nums = list(range(1,n+1))
        def helper(arr, k):
            if k <= 0 or not arr:
                return arr
            if len(arr) == k+1:
                return [arr[0],arr[-1]]+helper(arr[1:-1],k-2)
            elif k < len(arr)-1:
                return [arr[0]]+helper(arr[1:],k)
            else:
                return arr
        return helper(nums,k)