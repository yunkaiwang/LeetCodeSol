class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int area1 = (D - B) * (C - A);
        int area2 = (H - F) * (G - E);
        
        if (F >= D || H <= B || C <= E || G <= A) // no overlap area
            return area1 + area2;
        
        int overlap = (Math.min(D, H) - Math.max(B, F)) * (Math.min(C, G) - Math.max(A, E));
        return area1 + area2 - overlap;
    }
}