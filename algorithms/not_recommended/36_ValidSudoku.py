"""
Not an interesting question to work on, simply checks if there are 1-9 in each row, column, block
"""
class Solution:
    def isValidSudoku(self, board):
        """
        O(n^2) solution, runs in 80ms, beats 98%
        """
        row_dict = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        col_dict = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        brick_dict = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        for i in range(9):
            for j in range(9):
                cur_num = board[i][j]
                if cur_num != ".":
                    brick_num = (i // 3) * 3 + (j//3)
                    if cur_num in row_dict[i] or cur_num in col_dict[j] or cur_num in brick_dict[brick_num]:
                        return False
                    row_dict[i][cur_num] = 1
                    col_dict[j][cur_num] = 1
                    brick_dict[brick_num][cur_num] = 1
        return True