class Solution:
    def totalNQueens(self, n):
        """
        I thought there exist some connection between n and the number of solutions in a n by n board, but there isn't any known formula for this (based on Wikipedia), so the only way is to explord all possibilities like we did in the previous one, but now we are keep tracking of the number of solutions instead
        """
        if n == 2 or n == 3:
            return 0
        self.sols = 0
        
        col_dict = [False for _ in range(n)]
        diagonal_dict = {}
        for i in range(2 * n - 1):
            diagonal_dict[(i, "+")] = False
            diagonal_dict[(i, "-")] = False
        
        def dfs(b, c_r, col_dict, diagonal_dict):
            if c_r == n:
                self.sols += 1
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
        return self.sols
        