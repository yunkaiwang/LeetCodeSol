class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        longest, cur_start = 0, 0
        
        for i, c in enumerate(s):
            if c in dic and dic[c] >= cur_start:
                cur_start = dic[c] + 1
            else:
                longest = max(longest, i - cur_start + 1)
            dic[c] = i
            
        return longest