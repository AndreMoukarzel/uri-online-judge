class Graph:
    def __init__(self, ver_num):
        self.V = ver_num
        self.visited = [False] * (self.V)
        self.graph = []
        for v in range(ver_num):
            self.graph.append([])
   
   
    def getEdges(self):
        edges = [i for i in map(int, input().split())]
        for i in range(0, len(edges), 2):
            self.addEdge(edges[i] - 1, edges[i + 1] - 1)
    
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    
    def dfsEndOrder(self, v, ended):
        border = [v]
        self.visited[v] = True
        
        while len(border) > 0:
            curr = border.pop()
            for u in self.graph[curr]:
                if self.visited[u] == False:
                    self.visited[u] = True
                    border.append(u)
            ended.append(curr)
   
    
    def dfs(self, v, this_scc, exits, reverse_graph):
        self.visited[v] = True
        this_scc.append(v)
        if len(reverse_graph[v]) > 0:
            exits.append(reverse_graph[v])
        for u in self.graph[v]:
            if self.visited[u] == False:
                self.dfs(u, this_scc, exits, reverse_graph)
    
    
    def getReverseGraph(self):
        g = Graph(self.V)
        for v in range(self.V):
            for u in self.graph[v]:
                g.addEdge(u, v)
        return g
  

    def getSinks(self):
        ended = []
        for v in range(self.V):
            if self.visited[v] == False:
                self.dfsEndOrder(v, ended)
  
        gr = self.getReverseGraph()
        scc = []
        exits = []
        i = 0
        while ended:
            u = ended.pop()
            if gr.visited[u] == False:
                scc.append([])
                exits.append([])
                gr.dfs(u, scc[i], exits[i], self.graph)
                i += 1

        is_sink = [True] * len(scc)
        for i in range(len(scc)):
            for edges in exits[i]:
                for u in edges:
                    if u not in scc[i]:
                        is_sink[i] = False
            if is_sink[i]:
                for v in scc[i]:
                    print(v + 1, end=" ")
        print()


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
  

g.getSinks()

"""
inp = input()
while inp != 0:
    v, e = map(int, inp.split())
    
    g = Graph(v)
    g.getEdges()
    g.getSinks()
    
    inp = input()
"""