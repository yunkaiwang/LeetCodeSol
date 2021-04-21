class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        heap = []
        m, n = len(mat), len(mat[0])
        indices = [0] * m
        curSum = sum(mat[row][col] for row, col in enumerate(indices))
        heapq.heappush(heap,(curSum,)+tuple(indices))
        visited = set()
        while k>1:
            item = heapq.heappop(heap)
            indices = list(item[1:])
            curSum = item[0]
            nextSum = float('inf')
            for row, col in enumerate(indices):
                if col < n-1 :
                    indices[row] = indices[row]+1
                    if tuple(indices) not in visited:
                        nextSum = curSum - mat[row][col] + mat[row][col+1]
                        heapq.heappush(heap, (nextSum,)+tuple(indices))
                        visited.add(tuple(indices))
                    indices[row] = indices[row]-1
            k -= 1

        return heapq.heappop(heap)[0]