from itertools import permutations

def calculate_distance(matrix, path):
    distance = 0
    for i in range(len(path) - 1):
        distance += matrix[path[i]][path[i+1]]
    distance += matrix[path[-1]][path[0]]  # return to the start
    return distance

def tsp_brute_force(matrix):
    n = len(matrix)
    min_path_distance = float('inf')
    best_path = None
    for path in permutations(range(n)):
        current_distance = calculate_distance(matrix, path)
        if current_distance < min_path_distance:
            min_path_distance = current_distance
            best_path = path
    return min_path_distance, best_path

# Test case
matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_distance, best_path = tsp_brute_force(matrix)
print(f"Output: {min_distance}")
print(f"Best path: {best_path}")
