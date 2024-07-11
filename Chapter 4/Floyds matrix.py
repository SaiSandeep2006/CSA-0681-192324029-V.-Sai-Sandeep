def floyd_warshall(n, edges):
    # Initialize the distance matrix with infinity
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Set the diagonal to zero
    for i in range(n):
        dist[i][i] = 0
    
    # Set the distances based on the edges
    for u, v, w in edges:
        dist[u][v] = w
    
    # Print the distance matrix before applying the algorithm
    print("Distance matrix before applying Floyd's Algorithm:")
    for row in dist:
        print(row)
    
    # Apply Floyd's Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Print the distance matrix after applying the algorithm
    print("\nDistance matrix after applying Floyd's Algorithm:")
    for row in dist:
        print(row)
    
    return dist

def find_city_with_max_neighbors_within_threshold(n, edges, distance_threshold):
    dist = floyd_warshall(n, edges)
    
    max_neighbors = -1
    city_with_max_neighbors = -1
    
    for i in range(n):
        neighbors = sum(1 for j in range(n) if dist[i][j] <= distance_threshold and i != j)
        if neighbors > max_neighbors:
            max_neighbors = neighbors
            city_with_max_neighbors = i
    
    return city_with_max_neighbors

# Input: n = 5, edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], distanceThreshold = 2
n = 5
edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
distance_threshold = 2

# Find the city with the maximum number of neighbors within the distance threshold
result = find_city_with_max_neighbors_within_threshold(n, edges, distance_threshold)
print("\nCity with the greatest number of neighbors within distance threshold:", result)

# Test Case a: Shortest path from C to A
edges_a = [[1, 0, 2], [0, 2, 3], [2, 3, 1], [3, 0, 6], [2, 1, 7]]
n_a = 4
dist_a = floyd_warshall(n_a, edges_a)
print("\nShortest path from C to A:", dist_a[2][0])  # Expected Output: 7

# Test Case b: Shortest path from E to C
edges_b = [[2, 0, 2], [0, 1, 4], [1, 2, 1], [1, 4, 6], [4, 0, 1], [0, 3, 5], [3, 4, 2], [4, 3, 4], [3, 2, 1], [2, 3, 3]]
n_b = 5
dist_b = floyd_warshall(n_b, edges_b)
print("\nShortest path from E to C:", dist_b[4][2])  
