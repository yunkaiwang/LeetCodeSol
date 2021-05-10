class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        neighbour = collections.defaultdict(list)
        order = []
        degree = [0] * numCourses

        for course, prereq in prerequisites:
            neighbour[prereq].append(course)
            degree[course] += 1

        queue = collections.deque()
        for course in range(numCourses):
            if degree[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            for nextCourse in neighbour[course]:
                degree[nextCourse] -= 1
                if degree[nextCourse] == 0:
                    queue.append(nextCourse)
            order.append(course)
        return order if len(order) == numCourses else []
