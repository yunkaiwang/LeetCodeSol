class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        if x < 0:
            res = int("-" + x_str[::-1][:-1])
        else:
            res = int(x_str[::-1])
        
        upper_bound = 2 ** 31 - 1
        lower_bound = - upper_bound - 1
        if res > upper_bound or res < lower_bound:
            return 0 # overflow
        
        return res