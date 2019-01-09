class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        """
        long but very easy to understand solution without using string strip function.
        we first try to find the first non-whitespace character,
        then whenever we meet a new non-numerical character, we break, otherwise we keep adding the current character to the current string, and at the end, we check if the stirng is out of bound, if not, we return it
        """
        res = ""
        metFirstChar = False
        index = 0
        l = len(str)
        
        while index < l:
            char = str[index]
            index += 1
            if char == " ": # ignore all white space
                if metFirstChar:
                    break
                continue
            elif not metFirstChar and (char == "+" or char == "-"):
                res += char
                metFirstChar = True
                continue
            elif char.isdigit():
                metFirstChar = True
                res += char
            else:
                # first non-whitespace character is not digit or sign
                if not metFirstChar:
                    return 0
                else: # there are additional characters after the numeric characters
                    break
        
        if res == "" or res == "-" or res == "+":
            return 0
        res = int(res)
        
        INT_MAX = 2 ** 31 - 1
        INT_MIN = - INT_MAX - 1
        
        if res > INT_MAX:
            return INT_MAX
        elif res < INT_MIN:
            return INT_MIN
        else:
            return res