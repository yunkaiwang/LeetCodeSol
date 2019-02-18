class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        c, e = 1, nums[0]
        for num in nums[1:]:
            if c == 0:
                c = 1
                e = num
            elif num == e:
                c += 1
            else:
                c -= 1
        return e
                    