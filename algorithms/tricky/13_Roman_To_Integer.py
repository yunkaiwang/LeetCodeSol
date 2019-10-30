class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result, i = 0, 0
        while i < len(s):
            char = s[i]
            if i < len(s) - 1 and dict[char] < dict[s[i+1]]:
                result += dict[s[i+1]] - dict[char]
                i += 1
            else:
                result += dict[char]
            i += 1
        return result