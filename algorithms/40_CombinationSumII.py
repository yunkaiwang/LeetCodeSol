class Solution:

    def combinationSum2(self, candidates, target):
        """
        Modified DFS, running much faster, avoid many recursive calls, and don't need to use a set anymore
        """
        self.sols = []
        candidates.sort()
        self.dfs(target, [], candidates, 0)
        return self.sols
        
    def dfs(self, remaining, cur_list, candidates, cur_start_index):
        for i in range(cur_start_index, len(candidates)):
            cand = candidates[i]
            if cand > remaining:
                return
            if i != cur_start_index and cand == candidates[i-1]:
                continue
            elif cand == remaining:
                self.sols.append(cur_list + [cand])
                return
            else:
                self.dfs(remaining-cand, cur_list+[cand], candidates, i+1)
        

        """
        solution based on solution 1 from previous question, not sure why it's very inefficient here
        """
    def combinationSum2(self, candidates, target):
        from copy import deepcopy
        dict = {0: [([], {})]}
        for i in range(1, target + 1):
            dict[i] = []
        sols = set()
        candidates.sort()
        for j, candidate in enumerate(candidates):
            for i in range(target - candidate + 1):
                for temp in dict[i]:
                    if j in temp[1]:
                        continue
                    else:
                        d_copy = deepcopy(temp[1])
                        d_copy[j] = 1
                        dict[candidate + i].append((temp[0] + [candidate], d_copy))
        
        for sol, _ in dict[target]:
            sols.add(tuple(sol))
        return list(map(list, sols))
        

    """
    Solution based on DFS, again very inefficient
    """
    def combinationSum2(self, candidates, target):
        self.sols = set()
        candidates.sort()
        self.dfs(target, [], candidates, 0)
        return list(map(list, self.sols))
        
    def dfs(self, remaining, cur_list, candidates, cur_start_index):
        if remaining < 0:
            return
        elif remaining == 0:
            self.sols.add(tuple(cur_list))
        else:
            for i in range(cur_start_index, len(candidates)):
                self.dfs(remaining-candidates[i], cur_list+[candidates[i]], candidates, i+1)