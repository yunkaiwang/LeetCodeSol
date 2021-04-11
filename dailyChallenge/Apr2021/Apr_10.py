"""
Longest Increasing Path in a Matrix

Use a hashmap to store all visited positions, then
the solution becomes O(mn) instead of O(mn*4^x) where
x is the length of the longest increasing path
in the matrix
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        neighbour = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = {}
        m, n = len(matrix), len(matrix[0])
        def dfs(i, j):
            if (i, j) in visited:
                return visited[(i,j)]
            longest = 1
            for dir in neighbour:
                newX, newY = i+dir[0],j+dir[1]
                if 0<=newX<m and 0<=newY<n and matrix[newX][newY]>matrix[i][j]:
                    longest=max(longest,1+dfs(newX,newY))
            visited[(i,j)]=longest
            return longest
        longest = 1
        for i in range(m):
            for j in range(n):
                longest = max(longest,dfs(i,j))
        return longest