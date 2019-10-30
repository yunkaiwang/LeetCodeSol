class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        
        ans = set()
        def dfs(nums, l):
            if not nums:
                ans.add(tuple(l))
            else:
                dfs(nums[1:], nums[:1] + l)
                dfs(nums[1:], l)
                
        dfs(nums, [])
        return ans
        