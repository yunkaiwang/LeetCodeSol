class Solution:
    def mySqrt(self, x):
        """
        simple question, using Python standard math library is faster, and the other solution uses while loop, it can be furthur optimized by set i = i * i while i * i < x to save the runtime.
        """
        i = 0
        while i * i <= x:
            i += 1
        return i - 1
        
        return math.floor(math.sqrt(x))
        