class Solution:
    def isMatch(self, s, p):
        """
        O(len(s) + len(p)) solution, I start to think that
        question 10 cannot be done in this linear running time
        since the difference in the setting makes that we need
        to potentially search through all previous string in p
        to see if two strings match.
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
        optimized dynamic programming using O(n) space running in O(mn) time
        """
        m, n = len(s), len(p)

        dp = [False] * (n + 1)
        dp[0] = True  # empty string match the empty string
        for j in range(n):
            if p[j] == "*":
                dp[j + 1] = dp[j]

        for i in range(m):
            corner = dp[0]
            dp[0] = False
            for j in range(n):
                temp = dp[j + 1]
                dp[j + 1] = False
                if s[i] == p[j] or p[j] == "?":  # either a match string, or ?
                    dp[j + 1] |= corner
                elif p[j] == "*":
                    dp[j + 1] |= temp or dp[j]
                corner = temp

        return dp[-1]