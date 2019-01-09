class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        """simple but inefficient solution using string inverse"""
        if x < 0: # negative number cannot be palindrome
            return False
        x_str = str(x)
        x_str_inv = x_str[::-1]
        
        for index, char in enumerate(x_str):
            if char == x_str_inv[index]:
                continue
            else:
                return False
        return True

        """alternative solution, inverse half of the digits"""
        # if x < 0 or (x % 10 == 0 and not x == 0): # negative number cannot be palindrome, multiple of 10 cannot be palindrome
        #     return False
        
        # rev_x = 0
        # while x > rev_x:
        #     rev_x = rev_x * 10 + x % 10
        #     x = x // 10
        # return x == rev_x or x == rev_x // 10