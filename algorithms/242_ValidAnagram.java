class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
        HashMap<Character, Integer> smap = new HashMap<Character, Integer>();
        for (char c: s.toCharArray())
            smap.put(c, smap.getOrDefault(c, 0) + 1);
        for (char c: t.toCharArray())
            smap.put(c, smap.getOrDefault(c, 0) - 1);
        for (char c:smap.keySet()) {
            if (smap.get(c) != 0)
                return false;
        }
        return true;
    }
}