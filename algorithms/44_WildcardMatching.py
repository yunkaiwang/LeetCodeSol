class Solution:
    def isMatch(self, s, p):
        """
        O(len(s) + len(p)) solution, I start to think that question 10 cannot be done in this linear running time since the difference in the setting makes that we need to potentially search through all previous string in p to see if two strings match.
        """
        m, n, i, j = len(s), len(p), 0, 0
        star, s_star = -1, 1
        
        while i < m:
            if j < n and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            elif j < n and p[j] == "*":
                star = j
                s_star = i
                j += 1
            elif star != -1:
                j = star + 1
                s_star += 1
                i = s_star
            else:
                return False
            
        while j < n and p[j] == "*":
            j += 1
        return j == n
        

        """
        dynamic programming solution, not super efficient, a better solution should be available, like the one that I gave in question 10
        """
        table = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        
        table[0][0] = True
        
        for i in range(len(p)):
            table[i+1][0] = p[i] == "*" and table[i][0]
        
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == "*":
                    table[i+1][j+1] = table[i][j] or table[i+1][j] or table[i][j+1]
                else:
                    if p[i] == "?" or p[i] == s[j]:
                        table[i+1][j+1] = table[i][j]
        return table[-1][-1]