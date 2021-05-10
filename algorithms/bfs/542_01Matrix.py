class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        distance = [[0] * n for _ in range(m)]
        stations = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    distance[i][j] = 0
                    stations.append((i, j))
        curLevel = 1

        while stations:
            nextLevel = []
            for i, j in stations:
                if i > 0 and matrix[i - 1][j] == 1:
                    matrix[i - 1][j] = 0
                    distance[i - 1][j] = curLevel
                    nextLevel.append((i - 1, j))
                if i < m - 1 and matrix[i + 1][j] == 1:
                    matrix[i + 1][j] = 0
                    distance[i + 1][j] = curLevel
                    nextLevel.append((i + 1, j))
                if j > 0 and matrix[i][j - 1] == 1:
                    matrix[i][j - 1] = 0
                    distance[i][j - 1] = curLevel
                    nextLevel.append((i, j - 1))
                if j < n - 1 and matrix[i][j + 1] == 1:
                    matrix[i][j + 1] = 0
                    distance[i][j + 1] = curLevel
                    nextLevel.append((i, j + 1))
            stations = nextLevel
            curLevel += 1
        return distance