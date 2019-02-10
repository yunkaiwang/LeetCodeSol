class Solution:
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'List[str]':
        """
        has to check if the word is breakable before actually breaking it down as if not then I will get a memory limit exceed error on Leetcode
        """
        if not s or not wordDict:
            return []
        
        dict = {}
        max_len, min_len = 0, float('inf')
        for word in wordDict:
            if len(word) > max_len:
                max_len = len(word)
            if len(word) < min_len:
                min_len = len(word)
            
            dict[word] = True
        
        if not self.breakable(s, dict, min_len, max_len):
            return []
        
        l = [[] for _ in range(len(s) + 1)]
        l[0].append("")
        for i in range(len(s) - min_len + 1):
            if not l[i]:
                continue
            for j in range(min_len, max_len+1):
                if i + j <= len(s) and s[i: i+j] in dict:
                    for cur_str in l[i]:
                        l[i+j].append(cur_str + " " + s[i:i+j])
        
        return [str[1:] for str in l[-1]]

    def breakable(self, s, dict, min_len, max_len):
        dp = [True] + [False for _ in s]
        for i in range(len(s) - min_len + 1):
            if not dp[i]:
                continue
            for j in range(min_len, max_len+1):
                if i + j <= len(s) and s[i: i+j] in dict:
                    dp[i+j] = True
    
        return dp[-1]