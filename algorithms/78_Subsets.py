class Solution:
    def subsets(self, nums):
        """
        same as 77, not using python library, runs in 36ms beats 100%
        """
        res = []
        def dfs(left, a):
            if not left:
                res.append(a)
            else:
                dfs(left[1:], a + left[:1])
                dfs(left[1:], a)
        dfs(nums, [])
        return res
        