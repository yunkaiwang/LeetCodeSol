import math
class Solution:
    def clumsy(self, N: int) -> int:
        curRes = 0
        
        if N < 6:
            if N == 1:
                return 1
            elif N == 2:
                return 2
            elif N == 3:
                return 6
            else:
                return 7
        
        curRes = math.floor(N * (N-1) / (N-2)) + (N-3)
        N -= 4
        
        while N:
            if N < 6:
                if N == 1:
                    curRes -= 1
                elif N == 2:
                    curRes -= 2
                elif N == 3:
                    curRes -= 6
                elif N == 4:
                    curRes -= 5
                else:
                    curRes -= 5
                break
            
            curRes += math.floor((N * (N-1)) / (N-2)) * (-1) + (N-3)
            N -= 4
        return curRes