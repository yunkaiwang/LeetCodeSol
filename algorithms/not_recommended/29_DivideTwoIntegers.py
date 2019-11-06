class Solution:
    def divide(self, dividend, divisor):
        """
        This is not a good questions for two reasons:
        1. The edge cases are not necessary for the context of this question.
        2. The time limit setting forces you to simplify the while loop by continuing *2 if temp is less than the current dividend. However, we used multiplication in this case. If we are really wanting to solve this question without mul/div/mod operations, then we shouldn't allow multiplication in the while loop.

        Also, in real life, we can always use the div/mod operations instead.
        """
        INT_MIN = - 2 ** 31
        INT_MAX = - INT_MIN - 1
        if dividend > INT_MAX or dividend < INT_MIN:
            return INT_MAX
        
        quotient = 0
        neg_result = False
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            neg_result = True
            
        dividend, divisor = abs(dividend), abs(divisor)
        
        if divisor == 1:   
            return max(INT_MIN, -dividend) if neg_result else min(dividend, INT_MAX)
        
        while dividend >= divisor:
            temp = divisor
            temp_count = 1
            while temp + temp < dividend:
                temp += temp
                temp_count *= 2
            quotient += temp_count
            dividend -= temp
        return -quotient if neg_result else quotient
            