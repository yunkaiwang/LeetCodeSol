class Solution:
    def combinationSum3(self, k: 'int', n: 'int') -> 'List[List[int]]':
        if k > 9 or k < 1:
            return []
        if k == 1:
            if n < 10 and n > 0:
                return [[n]]
            else:
                return []
        
        res = []
        
        def dfs(lastNum, remaining_num, remaining_sum, cur_arr):
            if remaining_num == 0:
                if remaining_sum == 0:
                    res.append(cur_arr)
                return
            elif remaining_sum < 0:
                return
            
            for i in range(lastNum+1, 10):
                dfs(i, remaining_num-1, remaining_sum-i, cur_arr + [i])
        dfs(0, k, n, [])
        return res