class Solution:
    def permute(self, nums):
        """
        Solution based on DFS, O(n!) run time but that's the only way to generate all n! possible permutations
        """
        sols = []
        def dfs(perm, left_nums):
            if len(perm) == len(nums):
                sols.append(perm)
            else:
                for i, num in enumerate(left_nums):
                    dfs(perm + [num], left_nums[:i] + left_nums[i+1:])
        dfs([], nums)
        return sols