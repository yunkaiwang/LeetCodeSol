class Solution:
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        if not s or not wordDict:
            return False

        """
        use a hashmap to store all the word dict so that the time taken to find whether a word is in the word dict can be optimized
        """
        dict = {}
        max_len, min_len = 0, float('inf')
        for word in wordDict:
            if len(word) > max_len:
                max_len = len(word)
            if len(word) < min_len:
                min_len = len(word)
            
            dict[word] = True
        
        dp = [True] + [False for _ in s]
        for i in range(len(s) - min_len + 1):
            if not dp[i]:
                continue
            for j in range(min_len, max_len+1):
                if i + j <= len(s) and s[i: i+j] in dict:
                    dp[i+j] = True
        
        return dp[-1]