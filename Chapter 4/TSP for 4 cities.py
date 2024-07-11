import itertools

distances = {
    ('A', 'B'): 10, ('A', 'C'): 15, ('A', 'D'): 20, ('A', 'E'): 25,
    ('B', 'C'): 35, ('B', 'D'): 25, ('B', 'E'): 30,
    ('C', 'D'): 30, ('C', 'E'): 20,
    ('D', 'E'): 15
}

cities = ['A', 'B', 'C', 'D', 'E']

min_distance = float('inf')
best_route = None

for route in itertools.permutations(cities):
    route_distance = 0
    for i in range(len(route) - 1):
        route_distance += distances.get((route[i], route[i + 1]), float('inf'))
    if route_distance < min_distance:
        min_distance = route_distance
        best_route = route

print("Shortest Route:", ' -> '.join(best_route), ' -> ', best_route[0])
print("Total Distance:", min_distance)

