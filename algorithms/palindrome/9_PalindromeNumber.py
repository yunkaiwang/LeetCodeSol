class Solution:
    def isPalindrome(self, x):
        """simple solution using string inverse"""
        if x < 0 or (x != 0 and x % 10 == 0): # negative numbers or multiple of 10 cannot be palindrome
            return False
        return x == int(str(x)[::-1])

        """alternative solution, inverse half of the digits"""       
        # rev_x = 0
        # while x > rev_x:
        #     rev_x = rev_x * 10 + x % 10
        #     x = x // 10
        # return x == rev_x or x == rev_x // 10