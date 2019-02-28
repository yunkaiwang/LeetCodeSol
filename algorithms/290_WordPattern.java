class Solution {
    public boolean wordPattern(String pattern, String str) {
        /**
         * O(m+n) time with O(m+n) space solution
         */
        HashMap<Character, String> map = new HashMap<Character, String>();
        HashSet<String> mappedWord = new HashSet<String>();
        int pIndex = 0, sIndex = 0;
        while (pIndex < pattern.length() && sIndex < str.length()) {
            String currentWord = "";
            char currentChar;
            while (sIndex < str.length() && (currentChar = str.charAt(sIndex)) != ' ') {
                currentWord += currentChar;
                ++sIndex;
            }
            currentChar = pattern.charAt(pIndex);
            if (map.containsKey(currentChar) && !map.get(currentChar).equals(currentWord))
                return false;
            else if (!map.containsKey(currentChar) && mappedWord.contains(currentWord))
                return false;
            
            map.put(currentChar, currentWord);
            mappedWord.add(currentWord);
            ++pIndex;
            ++sIndex;
        }
        
        return pIndex == pattern.length() && sIndex >= str.length();
    }
}