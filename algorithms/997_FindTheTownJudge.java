class Solution {
    public int findJudge(int N, int[][] trust) {
        int[] trustCount = new int[N];
        int[] beTrustCount = new int[N];
        for (int[] t: trust) {
            ++trustCount[t[0]-1];
            ++beTrustCount[t[1]-1];
        }
        for (int i=0; i<N; ++i) {
            if (trustCount[i] == 0 && beTrustCount[i] == N-1)
                return i+1;
        }
        return -1;
    }
}