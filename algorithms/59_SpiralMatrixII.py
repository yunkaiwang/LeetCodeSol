class Solution:
    def generateMatrix(self, n):
        """
        O(n^2) space complexity and O(n^2) time complexity, no optimization we can do since we need to fill a n * n matrix entirely. Best run time 36ms beats 99%
        """
        ans = [[0]  * n for _ in range(n)]
        seen = [[False] * n for _ in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for i in range(n * n):
            ans[r][c] = i + 1
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < n and 0 <= cc < n and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans