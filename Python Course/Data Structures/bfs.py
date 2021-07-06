from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self,arg):
        visited=[False]*len(self.graph)
        queue=[]
        queue.append(arg)
        visited[arg]=True
        while queue:
            l=queue.pop(0)
            print(l)
            for i in self.graph[l]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
        
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
print(g.graph)
g.BFS(1)
