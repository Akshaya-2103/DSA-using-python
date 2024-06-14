def print_adj_list(graph):
    print("Adjacency list:")
    for node, neighbors in enumerate(graph):
        print(f"Node {node}: {', '}