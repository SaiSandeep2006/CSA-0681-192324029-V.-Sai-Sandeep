INF = 99999
def floyd_algorithm(graph):
    n = len(graph)
    dist = graph.copy()

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def simulate_link_failure(graph, node1, node2):
    graph[node1][node2] = INF
    graph[node2][node1] = INF

# Input: Distance matrix representing the graph
graph = [
    [0, 3, 8, INF, -4],
    [INF, 0, INF, 1, 7],
    [INF, 4, 0, INF, INF],
    [2, INF, -5, 0, INF],
    [INF, INF, INF, 6, 0]
]

# Applying Floyd's Algorithm
shortest_paths = floyd_algorithm(graph)

# Simulating link failure between Router B and Router D
simulate_link_failure(shortest_paths, 1, 3)

# Displaying the shortest path from Router A to Router F before link failure
print("Router A to Router F (Before Link Failure) =", shortest_paths[0][4])

# Displaying the shortest path from Router A to Router F after link failure
print("Router A to Router F (After Link Failure) =", shortest_paths[0][4])

