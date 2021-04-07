"""
Global and Local Inversions

O(n) solution

No need to count all global inversions, just check if there exists
any global inversions that are not local inversions
"""
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all(abs(i - v) <= 1 for i, v in enumerate(A))