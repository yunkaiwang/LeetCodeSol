class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.sums = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        for i, list in enumerate(matrix):
            for j, num in enumerate(list):
                self.sums[i+1][j+1] = self.sums[i+1][j] + self.sums[i][j+1] + num - self.sums[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1]-self.sums[row1][col2+1]-self.sums[row2+1][col1]+self.sums[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)