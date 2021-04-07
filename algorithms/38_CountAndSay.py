class Solution:
    def countAndSay(self, n):
        """
        The only hard thing is understanding the sequence,
        then implementing the solution is very straignt-forward,
        best runtime is 56ms, beats 96%
        """
        cur_str = "1"
        for _ in range(n - 1):
            res_str = ""
            cur_num = cur_str[0]
            cur_count = 1
            for char in cur_str[1:]:
                if char == cur_num:
                    cur_count += 1
                else:
                    res_str += str(cur_count) + cur_num
                    cur_num = char
                    cur_count = 1
            res_str += str(cur_count) + cur_num
            cur_str = res_str
        return cur_str