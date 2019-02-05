class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        i = 1
        while not res & i:
            i <<= 1
            
        num1, num2 = 0, 0
        for num in nums:
            if num & i:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]