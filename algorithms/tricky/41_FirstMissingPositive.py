class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        """
        the trick is use the array as the bucket and sort all the
        numbers in the array where the element >0 and <len(array),
        then we are able to go through the array and see which on
        is missing
        """
        i, n = 0, len(nums)
        while i < n:
            num = nums[i]
            if num == i + 1:
                i += 1
            else:
                if num > 0 and num < n:
                    switch = nums[num-1]
                    
                    if switch == num:
                        i += 1
                    else:
                        nums[num-1] = num
                        nums[i] = switch
                else:
                    i += 1
        for i, num in enumerate(nums):
            if num != i+1:
                return i+1
        return n+1
                        