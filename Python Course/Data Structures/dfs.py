from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_traverse(self,arg,visited):
        visited[arg]=True
        print(arg)
        for i in self.graph[arg]:
            if visited[i]==False:
                self.dfs_traverse(i,visited)

    def DFS(self,arg):
        visited=[False] * len(self.graph)
        self.dfs_traverse(arg,visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
print(g.graph)
g.DFS(1)
