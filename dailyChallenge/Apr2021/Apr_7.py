"""
Determine if String Halves Are Alike

O(n) solution with O(1) space
"""
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        numVowels = 0
        mid = len(s) // 2
        for i, c in enumerate(s):
            if c in vowels:
                if i < mid:
                    numVowels += 1
                else:
                    numVowels -= 1
        return numVowels == 0