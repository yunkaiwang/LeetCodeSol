class Solution {
    public int hIndex(int[] citations) {
        int[] count = new int[citations.length+1];
        for (int c: citations) {
            if (c < citations.length)
                count[c] += 1;
            else
                count[citations.length] += 1;
        }
        
        int c = 0;
        for (int i=citations.length; i>-1;--i) {
            c += count[i];
            if (c >= i)
                return i;
        }
        
        return 0;
    }
}