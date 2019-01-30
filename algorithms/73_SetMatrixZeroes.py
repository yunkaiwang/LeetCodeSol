class Solution:
    def setZeroes(self, matrix):
        """
        O(2mn) solution using O(m+n) space, beats 99.5%
        """
        m, n = len(matrix), len(matrix[0])
        arr = [0 for _ in range(m + n)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    arr[i] = 1
                    arr[m+j] = 1
        for i in range(m):
            for j in range(n):
                if arr[i] or arr[m + j]:
                    matrix[i][j] = 0
        
        """
        using constant extra space, and still O(mn) solution
        """
        m, n, first_col = len(matrix), len(matrix[0]), False
        
        for i in range(m):
            if not matrix[i][0]:
                first_col = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(1, n):
                matrix[0][i] = 0
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
        

        
        