# Бойков Максим
import random
from graph import Graph


def generate_er_graph(n: int, p: float) -> Graph:
    V = set(range(n))
    E = set()
    
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                E.add(frozenset({i, j}))
    
    return Graph(V, E)


if __name__ == "__main__":
    R = 0.00345
    graph = generate_er_graph(1347, R)
    print(len(graph.edges))
