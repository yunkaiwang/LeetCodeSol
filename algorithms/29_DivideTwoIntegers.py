class Solution:
    def divide(self, dividend, divisor):
        """
        not a good question, first of all the overflow setting is stupid, I have to use a if-statement to get rid of the overflow case, in real life, if an integer overflows, then the integer passed in should be between that range. Second, the question is useless as you can simply use division to accomplish this question.
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        
        count = 0
        dividend, divisor = abs(dividend), abs(divisor)
        if divisor == 1:
            return dividend if sign else -dividend
        
        while dividend >= divisor:
            temp = divisor
            temp_count = 1
            while temp + temp < dividend:
                temp += temp
                temp_count *= 2
            
            count += temp_count
            dividend -= temp
            
        return count if sign else -count
            