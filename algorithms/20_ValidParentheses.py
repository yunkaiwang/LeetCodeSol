class Solution:
    def isValid(self, s):
        """
        nothing to say, very straight forward using stack, O(n) solution with best runtime 52ms, beats 99%
        """
        if not s:
            return True
        
        list = [] # use list to keep track of brackets that are not mapped yet, used as stack
        # open brackets and their corresponding close bracket
        dict = {"(": ")", "[": "]", "{": "}"}
        
        for char in s:
            if char in dict:
                list.append(char)
            else:
                if len(list) > 0:
                    last_char = list.pop()
                else:
                    return False
                if not dict[last_char] == char:
                    return False
        return len(list) == 0