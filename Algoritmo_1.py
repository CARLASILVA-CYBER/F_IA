def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(f"Visitando: {node}")
            visited.add(node)
            if node in goal:
                print(f"Encontrado: {node}")
                return node
            stack.extend(graph[node][::-1])  # Inverte para manter ordem consistente
    return None

def bfs(graph, start, goal):
    queue = [start]
    visited = set()
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(f"Visitando: {node}")
            visited.add(node)
            if node in goal:
                print(f"Encontrado: {node}")
                return node
            queue.extend(graph[node])
    return None

# Teste do algoritmo
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': ['G1'],
    'D': ['G2'],
    'E': [],
    'F': [],
    'G1': [],
    'G2': []
}

goal_nodes = {'G1', 'G2'}

print("DFS:")
dfs(graph, 'S', goal_nodes)

print("\nBFS:")
bfs(graph, 'S', goal_nodes)
