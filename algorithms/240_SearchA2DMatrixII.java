class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        /**
         * O(m+n) algorithm
         */
        if (matrix.length == 0 || matrix[0].length == 0) return false;
        int row = 0, col = matrix[0].length-1;
        while (row < matrix.length && col > -1) {
            if (matrix[row][col] > target)
                --col;
            else if (matrix[row][col] < target)
                ++row;
            else
                return true;
        }
        return false;
    }
}