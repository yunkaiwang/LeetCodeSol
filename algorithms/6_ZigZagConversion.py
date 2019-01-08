class Solution:
    # don't really like this question, the only hard part for this question is understanding what the question is asking for, and find the potential relationship between the input string and the output string, each character in the input string has a corresponding index in the output string, and we simply need to add the characters one by one, it's not so interesting while finding the relationship as it can be very time consuming
    # O(n) solution
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if length <= numRows or numRows == 1:
            return s
        
        cycle = 2 * numRows - 2 # length of each cycle
        converted_str = ""
        
        for i in range(0, numRows - 1):
            index = i
            while index < length:
                converted_str += s[index]
                
                index2 = index + cycle - 2 * i
                if not i == 0 and index2 < length:
                    converted_str += s[index2]
                index += cycle
        
        index = numRows - 1
        while index < length:
            converted_str += s[index]
            index += cycle
        return converted_str

    # another way of completing this question using different idea, we simply pretend that we are walking down and up the rows, and we add the character we met to that list and we join the lists into 1
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step
        
        return ''.join(L)