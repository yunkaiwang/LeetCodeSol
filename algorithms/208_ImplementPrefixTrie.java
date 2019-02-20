class Trie {
    Trie[] children;
    boolean hasWordEndingHere;
    
    /** Initialize your data structure here. */
    public Trie() {
        children = new Trie[26];
        hasWordEndingHere = false;
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        char[] cArr = word.toCharArray();
        
        Trie curr = this;
        for (char c: cArr) {
            if (curr.children[c-'a'] == null) {
                curr.children[c-'a'] = new Trie();
            }
            curr = curr.children[c-'a'];
        }
        curr.hasWordEndingHere = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        char[] cArr = word.toCharArray();
        
        Trie curr = this;
        for (char c: cArr) {
            if (curr.children[c-'a'] == null) {
                return false;
            }
            curr = curr.children[c-'a'];
        }
        
        return curr.hasWordEndingHere;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        char[] cArr = prefix.toCharArray();
        
        Trie curr = this;
        for (char c: cArr) {
            if (curr.children[c-'a'] == null) {
                return false;
            }
            curr = curr.children[c-'a'];
        }
        return curr != null;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */