class TarjanSCC:
    def __init__(self, graph):
        self.graph = graph
        self.time = 0
        self.stack = []
        self.low_link = {}
        self.visited = set()
        self.sccs = []

    def _dfs(self, v):
        self.low_link[v] = self.time
        self.time += 1
        self.stack.append(v)
        self.visited.add(v)

        for neighbor in self.graph[v]:
            if neighbor not in self.low_link:
                self._dfs(neighbor)
                self.low_link[v] = min(self.low_link[v], self.low_link[neighbor])
            elif neighbor in self.stack:
                self.low_link[v] = min(self.low_link[v], self.low_link[neighbor])

        if self.low_link[v] == v:
            scc = []
            while True:
                u = self.stack.pop()
                scc.append(u)
                if u == v:
                    break
            self.sccs.append(scc)

    def find_sccs(self):
        for v in self.graph:
            if v not in self.low_link:
                self._dfs(v)
        return self.sccs

# EJEMPLO:
graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [5, 7],
    5: [6],
    6: [0, 2, 5],
    7: [3, 5, 8],
    8: [4, 7]
}

tarjan = TarjanSCC(graph)
sccs = tarjan.find_sccs()
print("Strongly Connected Components:")
for scc in sccs:
    print(scc)