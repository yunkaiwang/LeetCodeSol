from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = Counter(magazine)
        for c in ransomNote:
            if not c in map or map[c] == 0:
                return False
            map[c] -= 1
        return True