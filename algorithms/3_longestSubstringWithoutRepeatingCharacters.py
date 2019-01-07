class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
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
            if not char in _dict or _dict[char] < start:
                size += 1
            else:
                start = _dict[char]
                size = index - start
            
            _dict[char] = index

            # by using if-statement instead of max function, the runtime can be further improved
            max_length = max(max_length, size)
            
        return max_length

