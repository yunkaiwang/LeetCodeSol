"""
Pacific Atlantic Water Flow

O(mn) time solution with O(mn) space
where m = len(matrix), n = len(matrix[0])
"""
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        pacific = [[False] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = [(0, 0)]

        while stack:
            i, j = stack.pop()
            visited[i][j] = pacific[i][j] = True
            for (x, y) in directions:
                newX, newY = i + x, j + y
                if 0 <= newX < m and 0 <= newY < n and not visited[newX][newY] and \
                        ((newX == 0 or newY == 0) or matrix[newX][newY] >= matrix[i][j]):
                    stack.append((newX, newY))

        stack = [(m - 1, n - 1)]
        atlantic = [[False] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        while stack:
            i, j = stack.pop()
            visited[i][j] = atlantic[i][j] = True
            for (x, y) in directions:
                newX, newY = i + x, j + y
                if 0 <= newX < m and 0 <= newY < n and not visited[newX][newY] and \
                        ((newX == m - 1 or newY == n - 1) or matrix[newX][newY] >= matrix[i][j]):
                    stack.append((newX, newY))
        sol = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] == atlantic[i][j] == True:
                    sol.append([i, j])
        return sol