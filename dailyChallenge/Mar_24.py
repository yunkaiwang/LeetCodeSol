"""
Advantage Shuffle

Solution: O(nlog(n)) solution with O(n) space, I think this is
the best we can do on this question since we need to find out
for each number in b, the best number in a we should use to
beat that number, and to do so, we need to sort the arrays,
and sorting takes nlog(n) time.
"""
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        if not A or len(A) != len(B): return A
        A = sorted(A)
        sortedB = sorted(B)

        assigned = collections.defaultdict(list)
        remaining = []

        j = 0
        for i, num in enumerate(A):
            if num > sortedB[j]:
                assigned[sortedB[j]].append(num)
                j += 1
            else:
                remaining.append(num)

        return [assigned[num].pop() if assigned[num] else remaining.pop() for num in B]