class Solution:
    def fourSum(self, nums, target):
        """
        O(n^3) solution, based on 3sum, very straight forward but not so efficient, best answer I can think of is O(n^2 logn), the solution is that we make n^2 pairs of sums first, then we sort them, which takes time O(n^2 logn), then we use modified version of 2 sum to find pair of pairs that add up to the target, by modified version I mean that these two pairs should not have overlapping number(a number cannot be used twice), the other parts are same, and 2 sum can run in linear time in the size of the array, so this step takes O(n^2), so the total running time is O(n^2 log n).
        """
        
        if len(nums) < 4:
            return []
        
        nums.sort() # sort list
        sols = set()
        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                num1 = nums[i]
                num2 = nums[j]
                if i > 0 and num1 == nums[i - 1]:
                    continue
                dic = {}
                for x in nums[j+1:]:
                    if x not in dic:
                        dic[target-x-num1-num2] = 1
                    else:
                        sols.add((num1, num2, target-num2-num1-x, x))
            
        return [list(sol) for sol in sols]