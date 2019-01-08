class Solution:

    # easy to understand O(n^2) solution
    # simply expand around every possible center
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     # string is empty
    #     if not s:
    #         return ""
        
    #     length = len(s)
    #     m = 0
    #     cs = 0
    #     ce = 1
        
    #     for i in range(0, length):
    #         length1 = 1
    #         cur_left = i - 1
    #         cur_right = i + 1
    #         while cur_left >= 0 and cur_right < length and s[cur_left] == s[cur_right]:
    #             length1 += 2
    #             cur_left -= 1
    #             cur_right += 1
            
    #         if length1 > m:
    #             m = length1
    #             cs = cur_left + 1
    #             ce = cur_right
            
    #         length2 = 0
    #         cur_left = i
    #         cur_right = i + 1
            
    #         while cur_left >= 0 and cur_right < length and s[cur_left] == s[cur_right]:
    #             length2 += 2
    #             cur_left -= 1
    #             cur_right += 1
            
    #         if length2 > m:
    #             m = length2
    #             cs = cur_left + 1
    #             ce = cur_right
        
    #     return s[cs:ce]


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Manacher's Algorithm, O(n)
        # https://www.youtube.com/watch?v=nbTSfrEfo6M
        if not s:
            return ""
        
        t = "#" + "#".join(s) + "#"
        length = len(t)
        p = [0] * length
        m = 0
        cur_c, cur_r, ans = 0, 0, ""
        for i in range(1, length):
            if i < cur_r:
                dis = cur_r - i
                mir = p[cur_c * 2 - i]
                
                if dis > mir:
                    p[i] = mir
                else:
                    p[i] = dis
            else:
                p[i] = 1
            
            while i >= p[i] and p[i] + i < length and t[i+p[i]] == t[i-p[i]]:
                p[i] += 1
                
            if i + p[i] - 1 > cur_r:
                cur_r = i + p[i] - 1
                cur_c = i
            if p[i] > m:
                m = p[i]
                ans = s[(i + 1 - m)//2: (i - 1 + m)//2]
        return ans
        
        
        