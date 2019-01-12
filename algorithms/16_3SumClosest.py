class Solution:
    def threeSumClosest(self, nums, target):
        """
        n^2 solution using the same idea for 3-sum, use two points to do a linear search in order to find the closest sum, beats 85%
        """
        closest = float('inf')
        nums.sort() # sort list
        sols = set()
        for index, num in enumerate(nums[:-2]):
            if index > 0 and num == nums[index - 1]:
                continue
            
            l = index + 1
            r = len(nums) - 1
            while l < r:
                cur_sum = num + nums[l] + nums[r]
                if cur_sum > target:
                    r -= 1
                elif cur_sum < target:
                    l += 1
                else:
                    return target
                
                if abs(target - cur_sum) < abs(target - closest):
                    closest = cur_sum
            
        return closest
                

        """
        O(n^2 logn) solution, very inefficient, the basic idea if for n^2 pairs, find the number which make their total sum closest to the target using binary search, save us from n^3 to n^2 logn, but it's still not efficient
        """
        # def findClosest(nums, target):
        #     currentClosest = float('inf')
        #     l = 0
        #     r = len(nums) - 1
        #     while l <= r:
        #         m = (l + r) // 2
        #         if abs(target - nums[m]) < abs(target - currentClosest):
        #             currentClosest = nums[m]
        #         if nums[m] < target:
        #             l = m + 1
        #         elif nums[m] > target:
        #             r = m - 1
        #         else:
        #             return target
        #     return currentClosest
        
        # nums.sort()
        # closest_sum = float('inf')
        # print(nums)
        # for i in range(0, len(nums) - 1):
        #     for j in range(i + 1, len(nums) - 1):
        #         cur_sum = nums[i] + nums[j]
        #         closest_num = findClosest(nums[j + 1:], target - cur_sum)
                
        #         if abs(cur_sum + closest_num - target) < abs(target - closest_sum):
        #             closest_sum = cur_sum + closest_num
        # return closest_sum
                