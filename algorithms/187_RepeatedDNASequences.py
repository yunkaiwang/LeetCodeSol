class Solution:
    def findRepeatedDnaSequences(self, s: 'str') -> 'List[str]':
        l = []
        d = {}
        for i in range(len(s)-9):
            dna=s[i:i+10]
            d[dna] = 1 + (d[dna] if dna in d else 0)
        
        for key in d:
            if d[key] > 1:
                l.append(key)
        return l