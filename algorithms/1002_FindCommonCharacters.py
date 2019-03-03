class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        count = Counter(A[0])
        
        for word in A[1:]:
            wC = Counter(word)
            for key in count:
                count[key] = min(count[key], wC[key])
        
        res = []
        for key in count:
            res += [key] * count[key]
        return res