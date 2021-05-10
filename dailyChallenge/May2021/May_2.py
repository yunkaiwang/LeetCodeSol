class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: (c[1],c[0]))
        heap = []
        time = 0
        for duration, endDay in courses:
            heapq.heappush(heap,-duration)
            time += duration
            if time > endDay:
                time += heapq.heappop(heap)
        return len(heap)