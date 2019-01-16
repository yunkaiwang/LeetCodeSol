class Solution:
    def strStr(self, haystack, needle):
        """
        Two solutions are provided, one using naive approach, which takes time O(n * m) where n is length of haystack and m is length of needle, this takes 56ms(best run time). The other approach uses KMP algorithm, even though the run time is worse (since the test cases are so simple so KMP algorithm is too complicated for these cases), but it should be generally better for larger input and it can be easily modified so that it can be used to search all occurance of needle string in haystack string
        """
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

        """
        start of KMP algorithm
        
        table = [0] * (len(needle) + 1)
        table[0] = -1
        pos, cnd = 1, 0
        while pos < len(needle):
            if needle[pos] == needle[cnd]:
                table[pos] = table[cnd]
            else:
                table[pos] = cnd
                cnd = table[cnd]
                
                while cnd >= 0 and needle[pos] != needle[cnd]:
                    cnd = table[cnd]
            pos += 1
            cnd += 1
        table[pos] = cnd
        
        j, k = 0, 0
        
        while j < len(haystack):
            if needle[k] == haystack[j]:
                k += 1
                j += 1
                if k == len(needle):
                    return j - k
            else:
                k = table[k]
                if k < 0:
                    k += 1
                    j += 1
        return -1
        """