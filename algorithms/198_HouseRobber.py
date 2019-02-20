class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        m_rub, m_no_rub = 0, 0
        for num in nums:
            temp = m_no_rub
            m_no_rub = max(m_no_rub, m_rub)
            m_rub = temp + num
        return max(m_rub, m_no_rub)