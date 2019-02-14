class Solution:
    def minCut(self, s: 'str') -> 'int':
        """
        much faster solution, storing previous solution so that we don't need to check all possible substrings
        """
        def get_palindrome(s):
            dp = [[False] * len(s) for _ in range(len(s))]

            for end in range(len(s)):
                for st in range(end + 1):
                    if s[st] == s[end] and (end - st <= 2 or dp[st+1][end-1]):
                        dp[st][end] = True

            return dp
        
        is_palindrome = get_palindrome(s)
        n = len(s)
        dp = [i for i in range(-1, n+1)]
        
        for i in range(1, n + 1):
            for j in range(i):
                if is_palindrome[j][i-1]:
                    dp[i+1] = min(dp[i+1], dp[j+1] + 1)
        
        return dp[-1] - 1
        """
        accepted solution, but running extremely slow, since it's checking all possible substrings is palindrome
        """
        def isPalindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        if not s:
            return 0
        
        mem = {}
        dp = [-1] + [float('inf') for _ in s]
        for i in range(len(s)):
            for j in range(i+1):
                if (s[j:i+1] in mem and mem[s[j:i+1]]) or (not s[j:i+1] in mem and isPalindrome(s[j:i+1])):
                    mem[s[j:i+1]] = True
                    dp[i+1] = min(dp[i+1], dp[j] + 1)
                else:
                    mem[s[j:i+1]] = False
        
        return dp[-1]