class Solution:
    def combine(self, n, k):
        """
        solution not using Python library, runs in 108ms beats 96%
        """
        res = []
        def dfs(i, r, a):
            if r == 0:
                res.append(a)
            else:
                for j in range(i, n - r + 1):
                    dfs(j + 1, r-1, a + [j + 1])
        dfs(0, k, [])
        return res
        