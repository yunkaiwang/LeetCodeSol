class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        visited = {}
        i = n
        while i > 0:
            cells = [0] + [1 if cells[j-1]==cells[j+1] else 0 for j in range(1,7)] + [0]
            tupleCells = tuple(cells)
            diff = i
            if tupleCells in visited:
                diff = visited[tupleCells] - i
            visited[tupleCells] = i
            i = (i-1)%diff
        return cells