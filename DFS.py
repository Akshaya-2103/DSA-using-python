#Adjaceny list
#Stack
def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return result

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = 'A'
print("DFS Traversal starting from node 'A': ")
print(dfs(graph, start_node))  # Output: ['A', 'C', 'F', 'E', 'B', 'D']