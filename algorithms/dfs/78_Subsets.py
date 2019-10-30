class Solution:
    def subsets(self, nums):
        ans = []
        
        def dfs(nums, l):
            if not nums:
                ans.append(l)
            else:
                dfs(nums[1:], l+nums[:1])
                dfs(nums[1:], l)
        
        dfs(nums, [])
        return ans
        