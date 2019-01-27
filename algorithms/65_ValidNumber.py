class Solution:
    def isNumber(self, s):
        """
        really not a good question, too many cases to think of, but other than using a lot of variables to check whether the current string is valid or not, O(n) solution is very easy to be thought of. Best runtime 60ms beats 100%
        """
        metNum, metE, exValid, metDot, metSign, metSignInE = False, False, True, False, False, False
        
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        j = len(s) - 1
        while s[j] == " " and j > -1:
            j -= 1
        while i <= j :
            c = s[i]
            if c == " ":
                return False
            if c.isdigit():
                metNum = True
                exValid = True
            elif c == ".":
                if metE or metDot:
                    return False
                
                metDot = True
            elif c == "e":
                if metE or not metNum:
                    return False
                metE = True
                exValid = False
            elif c == "+" or c == "-":
                if metE:
                    if metSignInE:
                        return False
                    else:
                        if exValid:
                            return False
                else:
                    if metSign or metDot:
                        return False
                    if metNum:
                        return False
                    metSign = True
            else:
                return False
            i += 1
        return metNum and exValid