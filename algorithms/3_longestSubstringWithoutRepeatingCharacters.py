class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        68ms approach
        """
        if not s:
            return 0
    
        dict = {}
        cur_start, max_len = 0, 0
        
        for i, c in enumerate(s):
            if c in dict and dict[c] >= cur_start:
                cur_start = dict[c] + 1
            else:
                max_len = max(i - cur_start + 1, max_len)
            dict[c] = i
        return max_len
        
        """104ms approach
        max_length = 0 # initialize to 0
        _set = [] # current substring
        
        for char in s:
            if char in _set:
                max_length = max(max_length, len(_set))
                del _set[0:_set.index(char) + 1]
            _set.append(char)
            max_length = max(max_length, len(_set))
        return max_length
        """

        """76ms approach"""
        max_length = 0 # initialize to 0
        _dict = {} # current substring
        start = 0
        size = 0
        
        for index, char in enumerate(s):

            # if the character has not been met yet or the last appearance of the character is before the current starting character, then we add the character
            if not char in _dict or _dict[char] < start:
                size += 1
            else:
                start = _dict[char]
                size = index - start
            
            _dict[char] = index

            # by using if-statement instead of max function, the runtime can be further improved (64ms)
            max_length = max(max_length, size)
            
        return max_length

