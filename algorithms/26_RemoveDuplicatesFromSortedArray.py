class Solution:
    def removeDuplicates(self, nums):
        # O(n) solution is obvious, nothing to say about this question
        if not nums or not len(nums):
            return 
        count = 1
        cur_num = nums[0]
        
        for index in range(len(nums)):
            if not nums[index] == cur_num:
                cur_num = nums[index]
                nums[count] = cur_num
                count+=1
        return count