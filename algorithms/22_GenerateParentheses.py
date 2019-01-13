class Solution:
    def generateParenthesis(self, n):
        """
        Solution based on DFS, best runtime 56ms
        """
        sol = []
        
        def dfs(cur_str, o, c):
            if o==n and o==c:
                sol.append(cur_str)
            else:
                if o < n:
                    dfs(cur_str + "(", o + 1, c)
                if c < o:
                    dfs(cur_str + ")", o, c+1)
        dfs("", 0, 0)
        return sol