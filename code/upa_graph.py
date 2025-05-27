# Бойков Максим
import random
from graph import Graph


class UPATrial:
    def __init__(self, num_nodes: int) -> None:
        self._num_nodes = num_nodes
        self._node_numbers = []
        for node in range(num_nodes):
            self._node_numbers.extend([node] * (num_nodes - 1))
    
    def run_trial(self, num_nodes: int) -> set:
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        self._node_numbers.extend([self._num_nodes] * num_nodes)
        for neighbor in new_node_neighbors:
            self._node_numbers.append(neighbor)
        
        self._num_nodes += 1
        return new_node_neighbors


def generate_upa_graph(n: int, m: int) -> Graph:
    V = set(range(n))
    E = set()
    
    for i in range(m):
        for j in range(i + 1, m):
            E.add(frozenset({i, j}))
    
    upa_trial = UPATrial(m)
    
    for new_node in range(m, n):
        neighbors = upa_trial.run_trial(m)
        for neighbor in neighbors:
            E.add(frozenset({new_node, neighbor}))
    
    return Graph(V, E)


if __name__ == "__main__":
    P = 2
    graph = generate_upa_graph(1347, P)
    print(len(graph.edges))
