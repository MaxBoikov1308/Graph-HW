# Бойков Максим
import random


def generate_er_graph_set(n: int, p: float) -> tuple:
    V = set(range(n))
    E = set()
    
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                E.add(frozenset({i, j}))
    
    return (V, E)
