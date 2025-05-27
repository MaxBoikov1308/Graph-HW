# Бойков Максим

class Graph:
    def __init__(self, vertices=None, edges=None) -> None:

        self.vertices = set(vertices) if vertices else set()
        self.edges = set(frozenset(edge) for edge in edges) if edges else set()
    
    def add_vertex(self, vertex: str) -> None:
        self.vertices.add(vertex)
    
    def add_edge(self, vertex1: str, vertex2: str) -> None:
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise ValueError("Обе вершины должны быть в графе")
        self.edges.add(frozenset({vertex1, vertex2}))
    
    def remove_vertex(self, vertex: str) -> None:
        self.vertices.discard(vertex)
        self.edges = {edge for edge in self.edges if vertex not in edge}
    
    def remove_edge(self, vertex1: str, vertex2: str) -> None:
        self.edges.discard(frozenset({vertex1, vertex2}))
    
    def get_neighbors(self, vertex: str) -> set:
        if vertex not in self.vertices:
            raise ValueError("Вершина не существует в графе")
        return {v for edge in self.edges for v in edge if vertex in edge and v != vertex}
    
    def is_adjacent(self, vertex1: str, vertex2: str) -> bool:
        return frozenset({vertex1, vertex2}) in self.edges
    
    def __repr__(self) -> str:
        return f"Graph(vertices={self.vertices}, edges={self.edges})"
    
    def to_adjacency_dict(self) -> set:
        adj = {v: set() for v in self.vertices}
        for edge in self.edges:
            u, v = tuple(edge)
            adj[u].add(v)
            adj[v].add(u)
        return adj
    