class Solution:
    def plusOne(self, digits):
        """
        very simple question, just take care of those difference cases, best runtime 36ms beats 99%
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
        
        digits = [1] + digits
        return digits