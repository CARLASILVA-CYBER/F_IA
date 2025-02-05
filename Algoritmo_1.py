# Recarregar as bibliotecas após o reset
import networkx as nx
import matplotlib.pyplot as plt

# Recriar o grafo complexo
graph_complex = {
    'S': ['A', 'B', 'C'],
    'A': ['D', 'E'],
    'B': ['F', 'G'],
    'C': ['H'],
    'D': ['I'],
    'E': ['J', 'K'],
    'F': ['L'],
    'G': ['M'],
    'H': ['N', 'O'],
    'I': ['G1'],
    'J': [],
    'K': ['P'],
    'L': [],
    'M': ['G2'],
    'N': [],
    'O': ['Q'],
    'P': [],
    'Q': []
}

# Função para encontrar todos os caminhos usando DFS
def dfs_all_paths(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    
    if start in goal:
        return [path]
    
    paths = []
    for node in graph.get(start, []):
        if node not in path:  # Evitar ciclos
            new_paths = dfs_all_paths(graph, node, goal, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

# Função para encontrar todos os caminhos usando BFS
def bfs_all_paths(graph, start, goal):
    queue = [(start, [start])]
    paths = []

    while queue:
        (node, path) = queue.pop(0)
        
        if node in goal:
            paths.append(path)
            continue

        for neighbor in graph.get(node, []):
            if neighbor not in path:  # Evitar ciclos
                queue.append((neighbor, path + [neighbor]))

    return paths

# Definir os nós de destino
goal_nodes = {'G1', 'G2'}

# Obter os caminhos usando DFS e BFS
dfs_paths = dfs_all_paths(graph_complex, 'S', goal_nodes)
bfs_paths = bfs_all_paths(graph_complex, 'S', goal_nodes)

# Exibir os resultados
dfs_paths, bfs_paths

