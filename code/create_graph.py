# Бойков Максим
import random
from graph import Graph


def read_graph_from_file(filename: str) -> callable:
    graph = Graph()
    
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
                
            vertex = parts[0]
            neighbors = parts[1:]
            
            graph.add_vertex(vertex)
            
            for neighbor in neighbors:
                if neighbor not in graph.vertices:
                    graph.add_vertex(neighbor)
                graph.add_edge(vertex, neighbor)
    
    return graph


if __name__ == "__main__":
    graph = read_graph_from_file("hw4_data.txt")
    print(len(graph.edges))