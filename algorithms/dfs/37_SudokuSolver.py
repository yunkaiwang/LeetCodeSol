class Solution:
    """
    Solve the soduku using DFS, not very efficient, as the runtime is still exponential (possible) even though it's optimized to fill those positions with fewer possible entries. I don't like this solution though, as my favourite board game is soduku, and I know a few ways to solve a soduku board, but each of these methods are very very hard to implement, and itself is a NP-hard problem so no point of implementing those espicially I believe that using those solutions will degrade the performance of the solver if tried on LeetCode as those test cases are not so complicated, but if this solution was used on some baord with very few numbers, then the runtime will definitely explodes.
    """

    def solveSudoku(self, board):
        cols, rows, bricks, empty = [], [], [], set()
        for _ in range(9):
            cols.append(set(range(1, 10)))
            rows.append(set(range(1, 10)))
            bricks.append(set(range(1, 10)))
        for i in range(9):
            for j in range(9):
                cur_num = board[i][j]
                brick_num = (i // 3) * 3 + (j//3)
                if cur_num != ".":
                    rows[i].remove(int(cur_num))
                    cols[j].remove(int(cur_num))
                    bricks[brick_num].remove(int(cur_num))
                else:
                    empty.add((i, j))
        self.dfs(empty, board, cols, rows, bricks)
                    
    def dfs(self, empty, board, cols, rows, bricks):
            if len(empty) == 0:
                return True
            min_possible, m, n = 9, 0, 0
            for (i, j) in empty:
                brick_num = (i // 3) * 3 + (j//3)
                possible = rows[i] & cols[j] & bricks[brick_num]
                        
                if len(possible) < min_possible:
                    m, n = i, j
                    min_possible = len(possible)
            if min_possible == 0:
                return False
            brick_num = (m // 3) * 3 + (n//3)
            possible = rows[m] & cols[n] & bricks[brick_num]
            empty.remove((m, n))
            for num in possible:
                rows[m].remove(num)
                cols[n].remove(num)
                bricks[brick_num].remove(num)
                board[m][n] = str(num)
                if self.dfs(empty, board, cols, rows, bricks):
                    return True
                rows[m].add(num)
                cols[n].add(num)
                bricks[brick_num].add(num)
            board[m][n] = "."
            empty.add((m, n))
            return False
        
        