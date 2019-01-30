class Solution:
    def searchMatrix(self, matrix, target):
        """
        O(log(m) + log(n)) time algorithm where m is the # rows in the matrix, n is the # columns in the matrix, basic idea is use binary search to locate where the target should be, and then do binary search on that row to find where the target is
        """
        if not matrix or not matrix[0]:
            return False
        l_r, l_c = 0, 0
        r_r, r_c = len(matrix) - 1, len(matrix[0]) - 1
        
        while l_r < r_r:
            m = (l_r + r_r) // 2
            if matrix[m][0] > target:
                r_r = m - 1
            else:
                if matrix[m][-1] < target:
                    l_r = m + 1
                else:
                    r_r = m
        while l_c <= r_c:
            m = (l_c + r_c) // 2
            if matrix[l_r][m] > target:
                r_c = m - 1
            elif matrix[l_r][m] < target:
                l_c = m + 1
            else:
                return True
            
        return False
        