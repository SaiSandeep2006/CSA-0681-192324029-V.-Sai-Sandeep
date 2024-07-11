from collections import defaultdict
import heapq

def maxProbability(n, edges, succProb, start, end):
    graph = defaultdict(list)
    for i, (a, b) in enumerate(edges):
        prob = succProb[i]
        graph[a].append((b, prob))
        graph[b].append((a, prob))

    pq = [(-1, start)]
    probs = [0] * n
    probs[start] = 1

    while pq:
        cur_prob, node = heapq.heappop(pq)
        cur_prob = -cur_prob

        if node == end:
            return cur_prob

        for neighbor, neighbor_prob in graph[node]:
            new_prob = cur_prob * neighbor_prob
            if new_prob > probs[neighbor]:
                probs[neighbor] = new_prob
                heapq.heappush(pq, (-new_prob, neighbor))

    return 0

# Example 1
n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2
print(maxProbability(n, edges, succProb, start, end))  # Output: 0.25000

# Example 2
n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.3]
start = 0
end = 2
print(maxProbability(n, edges, succProb, start, end))  # Output: 0.30000
