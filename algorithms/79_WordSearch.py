class Solution:
    def exist(self, board, word):
        """
        solution based on dfs, running time is exponential but there is nothing we can do about it since all those exponential paths may potentially be the solution
        """
        if not board:
            return False
        max_r, max_c = len(board), len(board[0])
        def findAvailablePos(r, c):
            pos = []
            if r == -1 and c == -1:
                return [(x,y) for x in range(max_r) for y in range(max_c)]
            if r - 1 > -1:
                pos.append((r-1, c))
            if r + 1 < max_r:
                pos.append((r+1, c))
            if c - 1 > -1:
                pos.append((r, c-1))
            if c + 1 < max_c:
                pos.append((r, c+1))
            return pos
                
        used = [[False for _ in range(max_c)] for _ in range(max_r)]
        
        def dfs(cur_used_arr, left_word, l_r, l_c):
            if not left_word:
                return True
            
            poses = findAvailablePos(l_r, l_c)
            for (r, c) in poses:    
                if not cur_used_arr[r][c] and board[r][c] == left_word[0]:
                    cur_used_arr[r][c] = True
                    if dfs(cur_used_arr, left_word[1:], r, c):
                        return True
                    cur_used_arr[r][c] = False
            return False
                    
        
        return dfs(used, word, -1, -1)