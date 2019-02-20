class WordDictionary {
    WordDictionary[] children;
    boolean hasWordEndingHere;
    
    public WordDictionary() {
        children = new WordDictionary[26];
        hasWordEndingHere = false;
    }
    
    public void addWord(String word) {
        if (word.length() == 0) {
            hasWordEndingHere = true;
            return;
        }
        
        if (children[word.charAt(0)-'a'] == null) {
            children[word.charAt(0)-'a'] = new WordDictionary();
        }
        children[word.charAt(0)-'a'].addWord(word.substring(1));
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
        if (word.length() == 0) {
            return this.hasWordEndingHere;
        }
        
        if (word.charAt(0) == '.') {
            for (WordDictionary child: children) {
                if (child != null && child.search(word.substring(1)))
                    return true;
            }
            return false;
        } else {
            if (children[word.charAt(0)-'a'] == null)
                return false;
            return children[word.charAt(0)-'a'].search(word.substring(1));
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */