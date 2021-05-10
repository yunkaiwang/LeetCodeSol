class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = {}
        dp[(0, n - 1)] = grid[0][0] + grid[0][n - 1]
        neighbor = [[0, 0], [1, 1], [1, -1], [1, 0], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]
        for i in range(1, m):
            newDP = collections.defaultdict(int)
            for r1, r2 in dp:
                for ne in neighbor:
                    newR1, newR2 = r1 + ne[0], r2 + ne[1]
                    # if out of dimension, or robot 2 is to the left or robot 1
                    if newR1 >= n or newR2 >= n or newR1 < 0 or newR2 < 0 or newR2 < newR1:
                        continue
                    elif newR1 == newR2:
                        newDP[(newR1, newR2)] = max(newDP[(newR1, newR2)], dp[(r1, r2)] + grid[i][newR1])
                    else:
                        newDP[(newR1, newR2)] = max(newDP[(newR1, newR2)],
                                                    dp[(r1, r2)] + grid[i][newR1] + grid[i][newR2])
            dp = newDP
        return max(dp[(i, j)] for i, j in dp)
