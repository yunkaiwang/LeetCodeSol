class Solution:
    def lengthOfLastWord(self, s):
        """
        nothing to say, so simple question, runs in 32ms beats 100%. Just read the string backwards and if you meet an empty space, return the number if indices you have visited
        """
        l = 0
        for c in s[::-1]:
            if c == " ":
                if l != 0:
                    return l
            else:
                l += 1 
        return l
        