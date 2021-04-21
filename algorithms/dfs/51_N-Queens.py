class Solution:
    def solveNQueens(self, n):
        """
        DFS solution, and I think this is the fastest way to solve the question as long as P != NP, runs in 56ms beats 99%
        """
        if n == 2 or n == 3:
            return []
        sols = []
        
        col_dict = [False for _ in range(n)]
        diagonal_dict = {}
        for i in range(2 * n - 1):
            diagonal_dict[(i, "+")] = False
            diagonal_dict[(i, "-")] = False
        
        def dfs(b, c_r, col_dict, diagonal_dict):
            if c_r == n:
                sols.append(b)
                return
            
            for col in range(n):
                if col_dict[col]:
                    continue
                a1 = c_r + col
                a2 = c_r + (n - 1) - col
                    
                if diagonal_dict[(a1, "+")] or diagonal_dict[(a2, "-")]:
                        continue
                
                new_row = ["."] * n
                new_row[col] = "Q"
                col_dict[col] = True
                diagonal_dict[(a1, "+")] = True
                diagonal_dict[(a2, "-")] = True
                dfs(b + ["".join(new_row)], c_r+1, col_dict, diagonal_dict)
                col_dict[col] = False
                diagonal_dict[(a1, "+")] = False
                diagonal_dict[(a2, "-")] = False
        board = []
        dfs(board, 0, col_dict, diagonal_dict)
        return sols