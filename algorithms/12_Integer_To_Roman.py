class Solution:
    def intToRoman(self, num):
        """
        straight forward and easy to understand solution
        """
        
        chars = ["I", "V", "X", "L", "C", "D", "M"]
        
        pos = 0
        roman = ""
        
        while num > 0:
            digit = num % 10
            num //= 10
            
            if digit < 4:
                roman = chars[pos] * digit + roman
            elif digit == 4:
                roman = chars[pos] + chars[pos + 1] + roman
            elif digit < 9:
                roman = chars[pos + 1] + chars[pos] * (digit - 5) + roman
            elif digit == 9:
                roman = chars[pos] + chars[pos + 2] + roman
            pos += 2
        return roman