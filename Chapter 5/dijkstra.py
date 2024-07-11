import heapq

def dijkstra(n, graph, source):
    dist = [float('inf')] * n
    dist[source] = 0
    min_heap = [(0, source)]
    
    while min_heap:
        current_dist, u = heapq.heappop(min_heap)
        
        if current_dist > dist[u]:
            continue
        
        for v in range(n):
            if graph[u][v] != float('inf') and current_dist + graph[u][v] < dist[v]:
                dist[v] = current_dist + graph[u][v]
                heapq.heappush(min_heap, (dist[v], v))
    
    return dist


n1 = 5
graph1 = [[0, 10, 3, float('inf'), float('inf')], 
          [float('inf'), 0, 1, 2, float('inf')], 
          [float('inf'), 4, 0, 8, 2],
          [float('inf'), float('inf'), float('inf'), 0, 7], 
          [float('inf'), float('inf'), float('inf'), 9, 0]]
source1 = 0
print("5) ",dijkstra(n1, graph1, source1))  