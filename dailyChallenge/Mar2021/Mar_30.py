"""
Russian Doll Envelopes
"""
from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda e: (e[0], -e[1])) # nlog(n)
        max_idx = 0
        heights = [envelopes[0][1]] + [0] * (len(envelopes) - 1)
        for e in envelopes:
            idx = bisect_left(heights, e[1], hi=max_idx + 1)
            heights[idx] = e[1]
            max_idx = max(max_idx, idx)
        return max_idx + 1