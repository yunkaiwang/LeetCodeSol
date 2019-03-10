class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def helper(l, o, t):
            c = 0
            for i in range(1, len(l)):
                if l[i] == t:
                    continue
                elif o[i] == t:
                    c += 1
                else:
                    return -1
            return c
        
        m = float('inf')
        c = helper(A, B, A[0])
        if c != -1:
            m = min(m, c)
        c = helper(A, B, B[0])
        if c != -1:
            m = min(m, c+1)
        c = helper(B, A, B[0])
        if c != -1:
            m = min(m, c)
        c = helper(B, A, A[0])
        if c != -1:
            m = min(m, c+1)
        
        return -1 if m == float('inf') else m