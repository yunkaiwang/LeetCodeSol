class Solution:
    def removeDuplicates(self, nums):
        """
        O(n) solution using two pointers, use 1 pointer to remember where the next element should located, the other pointer to remember the position in the original array where we have read so that if there exist some elements who appear >2 times in the array, then second array will go ahead of the first pointer
        """
        if not nums:
            return 0
        
        c_i, i = 0, 0
        while i < len(nums):
            cur_num = nums[i]
            count = 1
            while i + count < len(nums) and nums[i + count] == cur_num:
                count += 1
            
            i += count
            nums[c_i] = cur_num
            c_i += 1
            if count >= 2:
                nums[c_i] = cur_num
                c_i += 1
        return c_i

        """
        solution that uses only 1 pointer, the reason that this one is more efficient than the previous one is that we know we need to loop through the entire array, so we don't need the second pointer, this one runs in 44ms beats 100%, last one runs in 48ms beasts 91%
        """
        i = 0
        for num in nums:
            if i < 2 or num > nums[i - 2]:
                nums[i] = num
                i += 1
        return i