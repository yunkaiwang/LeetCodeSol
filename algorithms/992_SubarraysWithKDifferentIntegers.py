class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        w1, w2 = {}, {}
        l1, l2 = 0, 0
        num_uni1, num_uni2 = 0, 0
        num_sol = 0
        
        for i, num in enumerate(A):
            w1[num] = 1 + (w1[num] if num in w1 else 0)
            w2[num] = 1 + (w2[num] if num in w2 else 0)
            if w1[num] == 1:
                num_uni1 += 1
            if w2[num] == 1:
                num_uni2 += 1
            
            while num_uni1 > K:
                w1[A[l1]] -= 1
                if w1[A[l1]] == 0:
                    num_uni1 -= 1
                l1 += 1
            
            while num_uni2 >= K:
                w2[A[l2]] -= 1
                if w2[A[l2]] == 0:
                    num_uni2 -= 1
                l2 += 1
            num_sol += l2 - l1
            
        return num_sol