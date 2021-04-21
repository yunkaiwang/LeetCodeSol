class Solution:
    def permuteUnique(self, nums):
        """
        Same idea as the last one, just need to sort it and ignore those duplicate cases
        """
        nums.sort()
        visited = [False for _ in range(len(nums))]
        sols = []
        def dfs(perm, visited):
            if len(perm) == len(nums):
                sols.append(perm)
            else:
                for i, num in enumerate(nums):
                    if visited[i]:
                        continue
                    elif i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                        continue
                    visited[i] = True
                    dfs(perm + [num], visited)
                    visited[i] = False
        dfs([], visited)
        return sols
        