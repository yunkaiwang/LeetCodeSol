class Solution {
    public void gameOfLife(int[][] board) {
        /**
         * O(m*n) solution using O(1) space, idea is use 3,4,5,6 to represent different states, for instance,
         * state 3 means the cell was live, and is still alive, 4 means the cell was dead, but become alive,
         * then we can compute the new state in-place with the help of these new states.
         */
        for (int i=0; i<board.length;++i) {
            for (int j=0; j<board[0].length;++j) {
                int liveNeighbor = 0;
                if (i > 0) {
                    if (board[i-1][j]%2 == 1) ++liveNeighbor;
                    if (j>0 && board[i-1][j-1]%2 == 1) ++liveNeighbor;
                    if (j<board[0].length-1 && board[i-1][j+1]%2 == 1) ++liveNeighbor;
                }
                if (i < board.length-1) {
                    if (board[i+1][j] == 1) ++liveNeighbor;
                    if (j>0 && board[i+1][j-1] == 1) ++liveNeighbor;
                    if (j<board[0].length-1 && board[i+1][j+1] == 1) ++liveNeighbor;
                }
                if (j>0 && board[i][j-1]%2 == 1) ++liveNeighbor;
                if (j<board[0].length-1 && board[i][j+1] == 1) ++liveNeighbor;
                
                if (board[i][j] == 1) {
                    if (liveNeighbor < 2 || liveNeighbor > 3)
                        board[i][j] = 5;
                    else
                        board[i][j] = 3;
                } else {
                    if (liveNeighbor == 3)
                        board[i][j] = 4;
                    else
                        board[i][j] = 6;
                }
            }
        }
        
        for (int i=0; i<board.length;++i) {
            for (int j=0; j<board[0].length;++j)
                board[i][j] = board[i][j]<5?1:0;
        }
    }
}