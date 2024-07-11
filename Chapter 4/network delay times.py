import heapq
from collections import defaultdict

def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    pq = [(0, k)]
    dist = {}
    
    while pq:
        time, node = heapq.heappop(pq)
        if node in dist:
            continue
        dist[node] = time
        for v, w in graph[node]:
            if v not in dist:
                heapq.heappush(pq, (time + w, v))
    
    return max(dist.values()) if len(dist) == n else -1

# Example Usage
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(network_delay_time(times, n, k))

times = [[1, 2, 1]]
n = 2
k = 1
print(network_delay_time(times, n, k))

times = [[1, 2, 1]]
n = 2
k = 2
print(network_delay_time(times, n, k))
