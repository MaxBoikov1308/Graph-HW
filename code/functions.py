# Бойков Максим
import random
from graph import Graph
from collections import deque


def compute_resilience(graph: Graph, attack_order: list) -> list:
    resilience = []
    temp_graph = Graph(graph.vertices.copy(), graph.edges.copy())
    
    resilience.append(largest_component_size(temp_graph))
    
    for vertex in attack_order:
        if vertex in temp_graph.vertices:
            temp_graph.remove_vertex(vertex)
            resilience.append(largest_component_size(temp_graph))
    
    return resilience

def largest_component_size(graph: Graph) -> int:
    visited = set()
    max_size = 0
    
    for vertex in graph.vertices:
        if vertex not in visited:
            queue = deque([vertex])
            visited.add(vertex)
            component_size = 1
            
            while queue:
                current = queue.popleft()
                for neighbor in graph.get_neighbors(current):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        component_size += 1
            
            if component_size > max_size:
                max_size = component_size
    
    return max_size

def random_order(graph: Graph) -> list:
    vertices = list(graph.vertices)
    random.shuffle(vertices)
    return vertices
