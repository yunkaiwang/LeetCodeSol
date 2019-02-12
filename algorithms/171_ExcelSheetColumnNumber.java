class Solution {
    public int titleToNumber(String s) {
        if (s == null || s == "") return 0;
        
        int currentNum = 0;
        for (int i=0; i<s.length(); ++i) {
            currentNum*=26;
            currentNum+=s.charAt(i)-'A'+1;
        }
        return currentNum;
    }
}