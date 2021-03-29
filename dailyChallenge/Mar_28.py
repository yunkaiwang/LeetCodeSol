"""
Reconstruct Original Digits from English

O(n) solution with O(1) space (at most 26 chars).
Don't like this question, the basic idea is
to identify a unique char for each digit
"""
class Solution:
    def originalDigits(self, s: str) -> str:
        sMap = collections.Counter(s)
        output = ""
        digitStr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        output += "0" * sMap['z']  # comfirm
        output += "1" * (sMap['o'] - sMap['z'] - sMap['u'] - sMap['w'])
        output += "2" * sMap['w']  # confirm
        output += "3" * (sMap['h'] - sMap['g'])
        output += "4" * sMap['u']  # confirm
        output += "5" * (sMap['f'] - sMap['u'])
        output += "6" * sMap['x']  # confirm
        output += "7" * (sMap['s'] - sMap['x'])
        output += "8" * sMap['g']  # confirm
        output += "9" * (sMap['i'] - sMap['g'] - sMap['x'] - sMap['f'] + sMap['u'])

        return output