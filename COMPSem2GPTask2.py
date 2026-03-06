def dijkstra(given_graph, start):

    distances = {node: float('inf') for node in given_graph}
    distances[start] = 0
    unvisited = list(given_graph.keys())

    while unvisited:

        current_node = None
        for node in unvisited:
            if current_node is None or distances[node] < distances[current_node]:
                current_node = node

        if distances[current_node] == float('inf'):
            break

        for neighbor, weight in given_graph[current_node].items():

            new_path = distances[current_node] + weight
            if new_path < distances[neighbor]:
                distances[neighbor] = new_path

        unvisited.remove(current_node)

    return distances

graph = {
    'Main Campus': {'JCC': 4, 'IOH': 2},
    'JCC': {'Asso': 3},
    'IOH': {'JCC': 1, 'Asso': 5},
    'Asso': {}
}

print(dijkstra(graph, 'Main Campus'))