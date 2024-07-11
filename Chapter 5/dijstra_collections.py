import heapq
from collections import defaultdict

def dijkstra(n, edges, source, target):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  
    
    dist = {i: float('inf') for i in range(n)}
    dist[source] = 0
    min_heap = [(0, source)]
    
    while min_heap:
        current_dist, u = heapq.heappop(min_heap)
        
        if u == target:
            return current_dist
        
        if current_dist > dist[u]:
            continue
        
        for v, weight in graph[u]:
            if current_dist + weight < dist[v]:
                dist[v] = current_dist + weight
                heapq.heappush(min_heap, (dist[v], v))
    
    return float('inf')


n1 = 6
edges1 = [(0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 2, 10), (1, 3, 15), 
          (2, 3, 11), (2, 5, 2), (3, 4, 6), (4, 5, 9)]
source1 = 0
target1 = 4
print("6) ",dijkstra(n1, edges1, source1, target1))  
