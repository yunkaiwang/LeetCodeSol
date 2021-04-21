class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        matrixSum = [[0] * (n) for _ in range(m)]

        count = 0
        for i in range(m):
            matrixSum[i][0] = matrix[i][0]
            for j in range(1, n):
                matrixSum[i][j] = matrix[i][j] + matrixSum[i][j - 1]

        for i in range(n):
            for j in range(i, n):
                dic = collections.defaultdict(int)
                dic[0] = 1
                curSum = 0
                for k in range(m):
                    curSum += matrixSum[k][j] - (matrixSum[k][i - 1] if i > 0 else 0)
                    count += dic[curSum - target]
                    dic[curSum] += 1
        return count
