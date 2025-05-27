from er_graph import generate_er_graph
from upa_graph import generate_upa_graph
from functions import random_order, compute_resilience
from create_graph import read_graph_from_file
import matplotlib.pyplot as plt
from typing import Dict, List
import numpy as np
from graph import Graph


computer_network = read_graph_from_file('.\hw4_data.txt')
er_graph = generate_er_graph(1347, 0.00345)
upa_graph = generate_upa_graph(1347, 2)

def plot_resilience_comparison(graphs: Dict[str, 'Graph'], 
                              attack_orders: Dict[str, List[str]],
                              title: str = "Сравнение устойчивости графов") -> None:
    plt.figure(figsize=(10, 6))
    
    resilience_data = {}
    for name, graph in graphs.items():
        resilience_data[name] = compute_resilience(graph, attack_orders[name])
    
    colors = plt.cm.tab10(np.linspace(0, 1, len(graphs)))
    
    for idx, (name, data) in enumerate(resilience_data.items()):
        x = np.arange(len(data))
        plt.plot(x, data, 
                label=name, 
                color=colors[idx],
                linewidth=2)
    
    plt.title(title, fontsize=14)
    plt.xlabel("Количество удаленных вершин", fontsize=12)
    plt.ylabel("Размер наибольшей компоненты", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    attack_orders = {
        "computer_network": random_order(computer_network),
        "er_graph": random_order(er_graph),
        "upa_graph": random_order(upa_graph)
    }
    
    plot_resilience_comparison(graphs={"computer_network": computer_network,
                                       "er_graph": er_graph,
                                       "upa_graph": upa_graph},
                                       attack_orders=attack_orders)
