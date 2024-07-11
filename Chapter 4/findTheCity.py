import heapq

def findTheCity(n, edges, distanceThreshold):
    graph = [[float('inf')] * n for _ in range(n)]
    
    for i, j, w in edges:
        graph[i][j] = graph[j][i] = w
    
    for i in range(n):
        graph[i][i] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    min_count = n
    res = -1
    
    for i in range(n):
        count = sum(dist <= distanceThreshold for dist in graph[i])
        if count <= min_count:
            min_count = count
            res = i
    
    return res

# Example 1
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
print(findTheCity(n, edges, distanceThreshold))  # Output: 3

# Example 2
n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2
print(findTheCity(n, edges, distanceThreshold))  # Output: 0
