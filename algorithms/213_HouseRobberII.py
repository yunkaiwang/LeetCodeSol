class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        if not nums: return 0
        if len(nums) < 2: return nums[0]
        return max(self.robHelper(nums, 0, len(nums)-1), self.robHelper(nums, 1, len(nums)))

    def robHelper(self, nums, i, j) -> 'int':
        m_rub, m_no_rub = 0, 0
        for num in nums[i:j]:
            temp = m_no_rub
            m_no_rub = max(m_no_rub, m_rub)
            m_rub = temp + num
        return max(m_rub, m_no_rub)