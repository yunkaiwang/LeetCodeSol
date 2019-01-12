class Solution:
    def romanToInt(self, s):
        """
        nothing to say about this problem, very straight forward, and linear time solution.
        """
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        num = 0
        index = 0
        while index < len(s):
            cur_num = dic[s[index]]
            if index + 1 < len(s) and dic[s[index+1]] > cur_num:
                num += dic[s[index+1]] - cur_num
                index += 2
            else:
                num += cur_num
                index += 1
        return num