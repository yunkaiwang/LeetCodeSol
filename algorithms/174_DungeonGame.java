class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        /**
         * bottom up DP solution
         */
        int row = dungeon.length-1, col = dungeon[0].length-1;
        dungeon[row][col] = dungeon[row][col] <= 0 ? -dungeon[row][col] + 1 : 1;
        for (int i=row-1; i>-1; --i) {
            dungeon[i][col] = dungeon[i][col] - dungeon[i+1][col] < 0 ? -(dungeon[i][col] - dungeon[i+1][col]) : 1;
        }
        
        for (int i=col-1; i>-1;--i) {
            dungeon[row][i] = dungeon[row][i] - dungeon[row][i+1] < 0 ? -(dungeon[row][i] - dungeon[row][i+1]) : 1;
        }
        
        for (int i=row-1; i>-1; --i) {
            for (int j=col-1; j>-1; --j) {
                dungeon[i][j] = dungeon[i][j] - Math.min(dungeon[i][j+1], dungeon[i+1][j]) < 0 ? -(dungeon[i][j] - Math.min(dungeon[i][j+1], dungeon[i+1][j])) : 1;
            }
        }
        
        return dungeon[0][0];
    }
}