class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        def getDirectionalPos(i, j, m, n):
            pos = []
            if i > 0:
                pos.append((i-1, j))
            if i < m-1:
                pos.append((i+1, j))
            if j > 0:
                pos.append((i, j-1))
            if j < n -1:
                pos.append((i, j+1))
            return pos
        m, n = len(grid), len(grid[0])
        
        rotten = []
        fresh = {}
        num_fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh[(i, j)] = True
                    num_fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        
        if num_fresh == 0: return 0
        minute = 0
        while num_fresh > 0:
            minute += 1
            new_rotten = []
            for (i, j) in rotten:
                for (p, q) in getDirectionalPos(i, j, m, n):
                    if (p, q) in fresh and fresh[(p, q)] == True:
                        fresh[(p, q)] = False
                        num_fresh -= 1
                        new_rotten.append((p, q))
            if len(new_rotten) == 0 and num_fresh > 0:
                return -1
            rotten = new_rotten
        return minute
                        
                