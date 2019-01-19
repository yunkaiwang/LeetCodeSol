class Solution:
    def multiply(self, num1, num2):
        """
        Solution without converting string to number directly, it calculates the product of every digit, it only beats 50%. However, it seems like most of the other answers are directly converting string to number, which is explicitly prohibited by the question.
        """ 
        res = 0
        digit = 1
        for c in num1[::-1]:
            cur_product = 0
            c = int(c)
            digit2 = 1
            for c2 in num2[::-1]:
                c2 = int(c2)
                cur_product += c2 * c * digit2
                digit2 *= 10
            res += cur_product * digit
            digit *= 10
        return str(res)