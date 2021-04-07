"""
O(n) initialilze time
O(n) space
O(1) pick time
"""
class Solution:

    def __init__(self, nums: List[int]):
        self.map = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.map[num].append(i)

    def pick(self, target: int) -> int:
        return self.map[target][randint(0, len(self.map[target])-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)