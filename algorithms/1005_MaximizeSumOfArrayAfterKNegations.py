import bisect

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        """
        O(nlog + Klogn) solution, since we need to flip K elements, so we first try to flip all the negative numbers, then if we still need to flip elements, we flip the smallest positive element
        """
        A.sort()
        while K:
            if A[0] < 0:
                temp = A.pop(0)
                bisect.insort_left(A,-temp)
            else:
                A[0] = -A[0]
            K-=1
        return sum(A)