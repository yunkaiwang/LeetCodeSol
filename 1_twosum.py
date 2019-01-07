class Solution(object):
    """
    There are other ways to solve this question as well, but the fastest way(O(n)) is to use a hashmap(dictionary in python), and simply put every number into the hashmap as key, and their indices as index, then for every number you just have to check if there exist a key-value pair in the hashmap with the difference as key.

    Other ways to solve the problem:
    - naive way: check n^2 pairs individually, very inefficient
    - sorting: sort all numbers, and for each number, do a binary search to find whether there exist such number so that their sum is the target, this approach will take O(nlogn) time since sorting take O(nlogn), then the loop runs n times, and each iteration takes O(logn) time.
    """

    """
    O(n) approach
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {} # initialize empty dictionary for storing
        
        for index, num in enumerate(nums):
            diff = target - num
            
            if diff in hashmap:
                return [hashmap[diff], index]
            
            hashmap[num] = index