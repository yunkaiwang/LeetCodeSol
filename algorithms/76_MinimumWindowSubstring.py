class Solution:
    def minWindow(self, s, t):
        t_dict = {}
        req = 0
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                req += 1
                t_dict[char] = 1
        
        cur_dict = {}
        l, r = 0, 0
        cur = 0
        ans = float("inf"), 0, 0
        while r < len(s):
            char = s[r]
            
            if char in cur_dict:
                cur_dict[char] += 1
            else:
                cur_dict[char] = 1
            
            if char in t_dict and cur_dict[char] == t_dict[char]:
                cur += 1
            
            while l < len(s) and cur == req:
                if r - l + 1 < ans[0]:
                    ans = r - l + 1, l, r
                
                char = s[l]
                
                cur_dict[char] -= 1
                if char in t_dict and cur_dict[char] < t_dict[char]:
                    cur -= 1
                l += 1
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]