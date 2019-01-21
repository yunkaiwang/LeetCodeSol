class Solution:
    def jump(self, nums):
        """
        Optimized to run in O(n) time, best run time 44ms beats 99%, similar idea but always update the max 2-jump position you can get so that we can get rid of the second for loop
        """
        length, max_r, next_r, jump = len(nums), 0, 0, 0
        for i in range(length):
            if i > max_r:
                jump += 1
                max_r = next_r
            if i + nums[i] > next_r:
                next_r = i + nums[i]
        return jump

        """
        potentially O(n^2) solution, idea is that you always try to go as far as you can with 2 steps, and remember the index which will give you the maximum 2-jump, best run time 52ms beats 95%
        """

        i, last_index, jump, next_i, cur_r = 0, len(nums) - 1, 0, -1, -1
        
        while i < last_index:
            num = nums[i]
            if i + num >= last_index:
                return jump + 1
            
            for j in range(1, num + 1):
                num2 = nums[i + j]
                if i + j + num2 >= cur_r:
                    cur_r = i + j + num2
                    next_i = i + j
            i = next_i
            jump += 1
            cur_r = -1
        
        return jump