class Solution:
    def reverse(self, x):
        """
        I have two solutions for this problem, similar runtime,
        one is using string inverse, and the other one simply recursively
        add the digits
        """
        # x_str = str(x)
        # if x < 0:
        #     res = int("-" + x_str[::-1][:-1])
        # else:
        #     res = int(x_str[::-1])
        # if abs(res) > 0x7FFFFFFF:
        #     return 0
        # return res

        # start of solution 2
        upper_b = 2 ** 31 - 1
        lower_b = - upper_b - 1
        if x == 0:
            return 0
        
        pos = abs(x)
        res = "" # result string
        
        while pos > 0:
            res += str(pos % 10)
            pos = pos // 10
        
        r = int(res)
        if x < 0:
            r = -r
            return r if r > lower_b else 0
        return r if r < upper_b else 0
    
        