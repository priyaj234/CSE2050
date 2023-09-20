from Priority_Queue import Entry, PQ_UL
class Graph:
    def __init__(self, V = (), E = ()):
        """Initializes/creates the graph"""
        self._V = set()
        self._E = set()
        self.nbrs = {}
        for v in V: self.add_vertex(v)
        for e in E: self.add_edge(e, v, 0)
    def __iter__(self):
        """a functions to iterate over the set of vertices"""
        return iter(self._V)
    def add_vertex(self, v):
        """a function to add a vertex to the set of vertices"""
        self._V.add(v)
    def remove_vertex(self, v):
        """a function to remove a vertex from the set of vertices"""
        if v in self._V:
           self._V.remove(v)
        else:
           raise KeyError("v is not in graph")
    def add_edge(self, u, v, wt):
        """a function to add a weighted edge into the neighbors set"""
        if u not in self.nbrs:
            self.nbrs[u] = {v:wt}
        if v not in self.nbrs:
            self.nbrs[v] = {u:wt}
        else:
            self.nbrs[u][v] = wt
            self.nbrs[v][u] = wt
    def remove_edge(self, u, v, wt):
        """a function to remove a weighted edge from the neighbors set"""
        if v in self.nbrs[u]:
            del self.nbrs[u][v]
        if u in self.nbrs[v]:
            del self.nbrs[v][u]
        else:
           raise KeyError("e is not in graph")
    def _neighbors(self, v):
        """a function iterating over the set of neighbors"""
        return iter(self.nbrs[v])

    def fewest_flights(self, city):
        """a function that finds the smallest number of flights it would take to get to each city in the graph from a preselected city"""
        tree = {}             
        cities = {}
        to_visit = [(None, city)] 
        cities[city] = 0
        while to_visit:
            a, b = to_visit.pop(0) 
            if b not in tree and b is not None:
                if a is not None:
                    cities[b] = cities[a] + 1
                tree[b] = a 
                for n in self.nbrs[b].keys():
                    if n not in tree: 
                        to_visit.append((b, n))

        return tree, cities 

    def shortest_path(self, city):
        """A function to find the shortest path to each city in the graph, using edge weights, from a preselected city"""
        tree = {}
        D = {city: 0}
        tovisit = PQ_UL()
        tovisit.insert((None,city), 0)
        for e in tovisit._entries:
            a, b = e.item, e.priority
            if b not in tree:
                tree[b] = a
                if a is not None:
                    D[b] = D[a] + self.nbrs[a][b]
                for n in self.nbrs(b):
                    tovisit.insert((b,n), D[b] + self.nbrs[b][n])
        return tree, D
    def minimum_salt(self, city):
        """A function to find the shortest path connecting all of the cities in the graph together in a path, using edge weights, from a preselected city"""
        city = next(iter(self._V))
        tree = {}
        D = {city:0}
        tovisit = PQ_UL()
        tovisit.insert((None, city), 0)
        for e in tovisit._entries:
            a, b = e.item, e.priority
            if b not in tree:
                tree[b] = a
                D[b] = self.nbrs[a][b]
                for n in self.nbrs[b]:
                    tovisit.insert((b,n),self.nbrs[b][n])
        return tree, D