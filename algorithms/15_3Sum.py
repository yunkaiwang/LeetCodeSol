class Solution:
    def threeSum(self, nums):
        """
        optimized solution beats 97%
        """
        if len(nums) < 3:
            return []
        count = {}
        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1
        
        sols = []
        
        uniqueNums = list(count.keys())
        uniqueNums.sort()
        
        for i, num in enumerate(uniqueNums):
            target = - num*2
            if target in count and ((target == num and count[num] > 2) or (target > num and count[num] > 1)):
                sols.append([num, num, -num*2])
            
            for j in range(i+1, len(uniqueNums)):
                target = - num - uniqueNums[j]
                if target in count and target >= uniqueNums[j]:
                    if target > uniqueNums[j] or count[uniqueNums[j]] >= 2:
                        sols.append([num, uniqueNums[j], target])
        return sols

        """
        Accepted O(n^2) solution based on the idea of 2sum, beats 86%
        """
        if len(nums) < 3:
            return []
        
        nums.sort() # sort list
        sols = set()
        for index, num in enumerate(nums[:-2]):
            if index > 0 and num == nums[index - 1]:
                continue
            if num > 0:
                break
            dic = {}
            for x in nums[index+1:]:
                if x not in dic:
                    dic[-x-num] = 1
                else:
                    sols.add((num, -num-x, x))
            
        return [list(sol) for sol in sols]
            

        """
        O(n^2) solution, exceed the time limit when tried on Leetcode, but it's correct
        """
        # sols = set() # all possible solutions
        # dic = {}
        
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         sum = nums[i] + nums[j]
        #         if sum in dic:
        #             dic[sum].append([i, j])
        #         else:
        #             dic[sum] = [[i, j]]
        
        # for i in range(len(nums)):
        #     if -nums[i] in dic:
        #         for a in dic[-nums[i]]:
        #             if i in a:
        #                 continue
                    
        #             sol = [nums[a[0]], nums[a[1]], nums[i]]
        #             sol.sort()
        #             sols.add(tuple(sol))
                     
        # r = [list(sol) for sol in sols]
        # return r