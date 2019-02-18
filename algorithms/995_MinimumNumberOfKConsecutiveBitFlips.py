class Solution:
    def minKBitFlips(self, A: 'List[int]', K: 'int') -> 'int':
        flip_pos = []
        num_flip = 0
        for i in range(len(A)):
            if flip_pos and i >= flip_pos[0] + K:
                flip_pos.pop(0)
            
            if i > len(A) - K:
                if A[i] == 0 and len(flip_pos) % 2 == 0:
                    return -1
                elif A[i] == 1 and len(flip_pos) % 2 == 1:
                    return -1
            elif A[i] == 1 and len(flip_pos) % 2 == 0:
                continue
            elif A[i] == 0 and len(flip_pos) % 2 == 1:
                A[i] = 1
            else:
                A[i] = 1
                num_flip += 1
                flip_pos.append(i)
            
        return num_flip