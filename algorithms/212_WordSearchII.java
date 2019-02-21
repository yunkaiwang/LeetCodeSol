class Solution {
    public TrieNode buildTrie(String[] words) {
        TrieNode root = new TrieNode();
        for (String w : words) {
            TrieNode p = root;
            for (char c : w.toCharArray()) {
                int i = c - 'a';
                if (p.next[i] == null) p.next[i] = new TrieNode();
                p = p.next[i];
           }
           p.word = w;
        }
        return root;
    }

    class TrieNode {
        TrieNode[] next = new TrieNode[26];
        String word = null;
    }
    public List<String> findWords(char[][] board, String[] words) {
        List<String> res = new LinkedList<String>();
        TrieNode root = buildTrie(words);
        for (int i=0; i<board.length; ++i) {
            for (int j=0; j<board[0].length; ++j) {
                dfs(res, board, root, i, j);
            }
        }
        return res;
    }
    
    public void dfs(List<String> res, char[][] board, TrieNode root, int i, int j) {
        char c = board[i][j];
        if (c == '#' || root.next[c - 'a'] == null) return;
        root = root.next[c - 'a'];
        if (root.word != null) {
            res.add(root.word);
            root.word = null; 
        }

        board[i][j] = '#';
        if (i > 0) dfs(res, board, root, i - 1, j); 
        if (j > 0) dfs(res, board, root, i, j-1); 
        if (i < board.length - 1) dfs(res, board, root, i+1, j); 
        if (j < board[0].length - 1) dfs(res, board, root, i, j+1); 
        board[i][j] = c;
    }
}