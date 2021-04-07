"""
Minimum Operations to Make Array Equal

Pure mathematical question, O(1) solution
"""
class Solution:
    def minOperations(self, n: int) -> int:
        return (n**2 - n%2) // 4