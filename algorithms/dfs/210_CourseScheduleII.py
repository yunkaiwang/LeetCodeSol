class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        neighbour = collections.defaultdict(list)

        for course, prereq in prerequisites:
            neighbour[prereq].append(course)

        visited = [0] * numCourses
        order = []

        def dfs(i):
            if visited[i] == 1:
                return False
            visited[i] = 1
            for nextI in neighbour[i]:
                if visited[nextI] != 2:
                    if not dfs(nextI): return False
            visited[i] = 2
            order.append(i)
            return True

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
        return order[::-1]
