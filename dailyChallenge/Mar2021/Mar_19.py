"""
Keys and Rooms

O(n) space and O(n) time solution.
It's based on DFS since it uses
stack, but can be changed to queue
if needed, the result will still
be the same and in that case,
it becomes a BFS solution.
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        canVisit = set()
        stack = [0]

        while stack:
            nextRoom = stack.pop()
            canVisit.add(nextRoom)
            for room in rooms[nextRoom]:
                if room not in canVisit:
                    stack.append(room)
        return len(canVisit) == len(rooms)