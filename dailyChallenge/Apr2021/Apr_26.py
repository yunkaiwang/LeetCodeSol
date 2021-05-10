class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i = 1
        ladderJump = []
        while i < len(heights):
            if heights[i] > heights[i - 1]:
                nextJump = heights[i] - heights[i - 1]
                if len(ladderJump) < ladders:
                    heapq.heappush(ladderJump, nextJump)
                else:
                    nextJump = heapq.heappushpop(ladderJump, nextJump)

                    if nextJump > bricks:
                        break
                    bricks -= nextJump

            i += 1
        return i - 1