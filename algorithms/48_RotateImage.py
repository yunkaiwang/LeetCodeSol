class Solution:
    def rotate(self, matrix):
        """
        Accepted solution, does in place change, but using similar idea
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i] 

        """
        one line solution using Python but it's not accepted by Leetcode,
        since the matrix will always remain unchanged, maybe because I
        didn't change the matrix in-place
        """
        matrix = [[matrix[i][j] for i in range(len(matrix))][::-1] for j in range(len(matrix[0]))]