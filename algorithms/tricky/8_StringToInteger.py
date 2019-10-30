class Solution:
    def myAtoi(self, str):
        res = ""
        metFirstChar = False
        index = 0
        
        while index < len(str):
            char = str[index]
            index += 1
            if char == " ":
                if metFirstChar: # white space after numeric values
                    break
                continue
            elif char == "+" or char == "-": # might be the sign
                if metFirstChar: # more than one sign or a sign after nemeric value
                    break
                metFirstChar = True
                res += char
            elif char.isdigit():
                metFirstChar = True
                res += char
            else:
                if not metFirstChar: # first non-whitespace character is not sign or numeric value
                    return 0
                break
        
        if not res or res == "+" or res == "-":
            return 0 # not a valid number
        
        upper_bound = 2**31 -1
        lower_bound = -upper_bound -1
        int_res = int(res)
        if int_res < lower_bound:
            return lower_bound
        elif int_res > upper_bound:
            return upper_bound
        return int_res