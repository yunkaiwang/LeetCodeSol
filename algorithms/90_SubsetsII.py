class Solution:
    def subsetsWithDup(self, nums):
        """
        similar to 78, only uses a set and sort the num before dfs
        """
        nums.sort()
        
        res = set()
        def dfs(left, a):
            if not left:
                res.add(tuple(a))
            else:
                dfs(left[1:], a + left[:1])
                dfs(left[1:], a)
        dfs(nums, [])
        return list(res)
        