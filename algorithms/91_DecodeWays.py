 class Solution:
    def numDecodings(self, s):
        if not s or s[0] == "0": return 0
        a = 1
        b = 1
        i = 1
        while i < len(s):
            if s[i] < "1":
                if s[i-1] > "2" or s[i-1] < "1":
                    return 0
                else:
                    c = a
            elif s[i-1] > "0" and s[i-1:i+1] < "27":
                c = b + a
            else:
                c = b
            i += 1
            a = b
            b = c
        return b
        