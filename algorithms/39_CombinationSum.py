class Solution:
    def combinationSum(self, candidates, target):
        """
        Solution based on dynamic programming
        """
        dict = {0: [[]]}
        for i in range(1, target + 1):
            dict[i] = []
        sols = set()
        for candidate in candidates:
            for i in range(target - candidate + 1):
                for temp in dict[i]:
                    dict[candidate + i].append(temp + [candidate])
            
        return dict[target]

        """
        Idea based on DFS, very inefficient, but it's still a solution
        """
        sols = []
        candidates.sort()
        def dfs(remaining, index, cur_list):
            if remaining < 0:
                return
            elif remaining == 0:
                sols.append(cur_list)
            else:
                for i in range(index, len(candidates)):
                    dfs(remaining - candidates[i], i, cur_list + [candidates[i]])
        dfs(target, 0, [])
        return sols