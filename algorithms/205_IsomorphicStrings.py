class Solution:
    def isIsomorphic(self, s: 'str', t: 'str') -> 'bool':
        map_for, map_bak = {}, {}
        for i, char in enumerate(s):
            if char in map_for and map_for[char] != t[i]:
                return False
            elif t[i] in map_bak and map_bak[t[i]] != char:
                return False
            else:
                map_for[char] = t[i]
                map_bak[t[i]] = char
        return True