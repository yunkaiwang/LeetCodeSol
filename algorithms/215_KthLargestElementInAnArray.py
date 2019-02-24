class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        s, e, l = [], [nums[0]], []
        
        for num in nums[1:]:
            if num < nums[0]:
                s.append(num)
            elif num == nums[0]:
                e.append(num)
            else:
                l.append(num)
        
        if k <= len(l):
            return self.findKthLargest(l, k)
        elif k - len(l) <= len(e):
            return e[0]
        else:
            return self.findKthLargest(s, k-len(l)-len(e))
        