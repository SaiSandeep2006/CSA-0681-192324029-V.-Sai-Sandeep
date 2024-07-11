
import itertools
import math
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
def tsp(cities):
    min_distance = float('inf')
    shortest_path = None
    for perm in itertools.permutations(cities[1:]):
        total_distance = 0
        path = [cities[0]] + list(perm) + [cities[0]]
        for i in range(len(path) - 1):
            total_distance += distance(path[i], path[i+1])
        if total_distance < min_distance:
            min_distance = total_distance
            shortest_path = path
    return min_distance, shortest_path
# Test Cases
cities1 = [(1, 2), (4, 5), (7, 1), (3, 6)]
shortest_distance1, shortest_path1 = tsp(cities1)
print("Test Case 1:")
print("Shortest Distance:", shortest_distance1)
print("Shortest Path:", shortest_path1)
