class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.visited = [False] * n
        self.index = [-1] * n
        self.curIndex = 0
        self.lowIndex = [-1] * n
        self.graph = collections.defaultdict(list)
        for v1, v2 in connections:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
        self.critical = []
        self.strongConnect(0)

        return self.critical

    def strongConnect(self, i, prev=-1):
        self.visited[i] = True
        self.lowIndex[i] = self.index[i] = self.curIndex
        self.curIndex += 1
        for to in self.graph[i]:
            if to == prev: continue
            if not self.visited[to]:
                self.strongConnect(to, i)
            self.lowIndex[i] = min(self.lowIndex[i], self.lowIndex[to])
            if self.lowIndex[to] > self.index[i]:
                self.critical.append((i, to))
