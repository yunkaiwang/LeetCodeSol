class Solution {
    public int numRookCaptures(char[][] board) {
        for (int i=0; i<8;++i) {
            for (int j=0; j<8;++j) {
                if (board[i][j] == 'R') {
                    int count = 0;
                    int k = i - 1;
                    while (k > -1) {
                        if (board[k][j] == 'p') {
                            ++count;
                            break;
                        } else if (board[k][j] == 'B')
                            break;
                        k -= 1;
                    }
                    k = i+1;
                    while (k < 8) {
                        if (board[k][j] == 'p') {
                            ++count;
                            break;
                        } else if (board[k][j] == 'B')
                            break;
                        k += 1;
                    }
                    k = j - 1;
                    while (k > -1) {
                        if (board[i][k] == 'p') {
                            ++count;
                            break;
                        } else if (board[i][k] == 'B')
                            break;
                        k -= 1;
                    }
                    k = j+1;
                    while (k < 8) {
                        if (board[i][k] == 'p') {
                            ++count;
                            break;
                        } else if (board[i][k] == 'B')
                            break;
                        k += 1;
                    }
                    return count;
                }
            }
        }
        return 0;
    }
}