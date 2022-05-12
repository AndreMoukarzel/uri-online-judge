class Graph:
    def __init__(self, ver_num, test=False):
        self.graph = []
        self.dist = []
        self.color = [] # 0 = white, 1 = gray, 2 = black
        self.stack = []
        self.V = ver_num
        for v in range(ver_num):
            self.graph.append([])
            self.dist.append(1)
            self.color.append(0)
            if not test:
                self.get_edges(v)
    
    def get_edges(self, v: int):
        edges = [i for i in map(int, input().split())]
        for i in range(edges[0]):
            u = edges[i + 1]
            self.add_edge(v, u - 1)
  
    def add_edge(self, v: int, u: int):
        self.graph[v].append(u)
    
    def dfs(self, u: int):
        if self.color[u] == 0:
            self.color[u] = 1
            for v in self.graph[u]:
                self.dist[v] = max(self.dist[v], self.dist[u] + 1)
                if self.dfs(v) == -1:
                    return -1
            self.color[u] = 2
            self.stack.append(u)
        elif self.color[u] == 1:
            return -1
        return 1
        
    def answer(self):
        for v in range(self.V):
            if self.color[v] == 0:
                if self.dfs(v) == -1:
                    return -1
        
        for u in reversed(self.stack):
            for v in self.graph[u]:
                self.dist[v] = max(self.dist[v], self.dist[u] + 1)
            
        max_dist = 1
        for dist in self.dist:
            max_dist = max(dist, max_dist)
        return max_dist

  
#g = Graph(6, test=True)
#g.add_edge(5, 2);
#g.add_edge(5, 0);
#g.add_edge(4, 0);
#g.add_edge(4, 1);
#g.add_edge(2, 3);
#g.add_edge(3, 1);
#g = Graph(3, test=True)
#g.add_edge(1, 2)
g = Graph(2, test=True)
g.add_edge(0, 1)
g.add_edge(1, 0)
  
print(g.answer())

"""
while True:
    try:
        size = int(input())
        g = Graph(size)
        print(g.answer())
        #print(g.graph)
    except EOFError:
        break
"""