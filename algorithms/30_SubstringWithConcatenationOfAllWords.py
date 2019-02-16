
class Solution:
    def findSubstring(self, s, words):
        """
        O(n^2) method using sliding window
        """
        if not s or not words: return []
        hashmap = {}
        for word in words:
            if word in hashmap:
                hashmap[word] = hashmap[word] + 1
            else:
                hashmap[word] = 1
        
        m = len(words)
        n = len(words[0])
        ret = []         
        
        for k in range(n):
            left = k
            dict = {}
            count = 0
            
            for j in range(k, len(s) - n + 1, n):
                word = s[j:j+n]
                if word in hashmap:
                    dict[word] = dict[word] + 1 if word in dict else 1
                    count += 1
                    while dict[word] > hashmap[word]:
                        dict[s[left:left+n]] -= 1
                        left += n
                        count -= 1
                    if count == m:
                        ret.append(left)
                else:
                    left = j+n
                    dict = {}
                    count = 0
                               
        return ret