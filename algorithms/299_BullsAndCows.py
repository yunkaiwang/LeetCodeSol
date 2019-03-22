from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        m = defaultdict(int)
        b, c = 0, 0
        
        for i, s in enumerate(secret):
            if guess[i] == s:
                b += 1
            else:
                if m[guess[i]] > 0:
                    c += 1
                if m[s] < 0:
                    c += 1
                
                m[guess[i]] -= 1
                m[s] += 1
        
        return "".join([str(b), "A", str(c), "B"])