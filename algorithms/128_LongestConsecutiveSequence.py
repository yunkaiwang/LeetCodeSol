class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> 'int':
        dict = {}
        for num in nums:
            dict[num] = True
        
        longest,cur = 0, 0
        for num in nums:
            if not num-1 in dict:
                cur = 1
                num += 1
                while num in dict:
                    cur += 1
                    num += 1
                
                if cur > longest:
                    longest = cur
        
        return longest