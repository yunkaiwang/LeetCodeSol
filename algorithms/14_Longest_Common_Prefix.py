class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        cur_prefix = ""
        cur_pos = 0
        should_continue = True
        while should_continue:
            if cur_pos >= len(strs[0]):
                break
            char = strs[0][cur_pos]
            for i in range(1, len(strs)):
                if cur_pos >= len(strs[i]) or not strs[i][cur_pos] == char:
                    should_continue = False
            if should_continue:
                cur_prefix += char
                cur_pos += 1
        return cur_prefix