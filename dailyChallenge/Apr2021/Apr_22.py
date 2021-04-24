class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        breaks = collections.defaultdict(int)
        minWall = float('inf')
        edges = set()
        for i, level in enumerate(wall):
            curCol = 0
            for brick in level:
                curCol += brick
                edges.add(curCol)
                breaks[curCol] -= 1
        sumLevel = sum(wall[0])
        if sumLevel == 1: return len(wall)
        for col in edges:
            if col == sumLevel: continue
            minWall = min(minWall, breaks[col]+len(wall))
        return minWall if minWall < float('inf') else len(wall)