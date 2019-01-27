class Solution:
    def addBinary(self, a, b):
        """
        Also very simple, just analyze those cases correctly and the answer is very obvious, O(len(a) + len(b)) time solution, best runtime 40ms beats 92%
        """
        i, j = len(a) - 1, len(b) - 1
        res, add_on = "", False
        
        while i > - 1 or j > -1:
            x = a[i] if i > -1 else "0"
            y = b[j] if j > -1 else "0"
            if x == "1":
                if y == "0":
                    if add_on:
                        res = "0" + res
                        add_on = True
                    else:
                        res = "1" + res
                else:
                    if add_on:
                        res = "1" + res
                    else:
                        res = "0" + res
                    
                    add_on = True
            else:
                if y == "0":
                    if add_on:
                        res = "1" + res
                        add_on = False
                    else:
                        res = "0" + res
                else:
                    if add_on:
                        res = "0" + res
                        add_on = True
                    else:
                        res = "1" + res
            i -= 1
            j -= 1
            
        if add_on:
            res = "1" + res
        return res
        
        