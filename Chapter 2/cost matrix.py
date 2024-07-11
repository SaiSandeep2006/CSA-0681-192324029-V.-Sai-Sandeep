import itertools
def total_cost(assignment, cost_matrix):
    return sum(cost_matrix[worker][task] for worker, task in assignment)
def assignment_problem(cost_matrix):
    workers = range(len(cost_matrix))
    min_cost = float('inf')
    optimal_assignment = None
    for permutation in itertools.permutations(workers):
        assignment = list(zip(permutation, range(len(cost_matrix))))
        cost = total_cost(assignment, cost_matrix)
        if cost < min_cost:
            min_cost = cost
            optimal_assignment = assignment
    return optimal_assignment, min_cost
# Test Cases
cost_matrix_1 = [[3, 10, 7], [8, 5, 12], [4, 6, 9]]
optimal_assignment_1, total_cost_1 = assignment_problem(cost_matrix_1)
print("Test Case 1:")
print("Optimal Assignment:", [(f"worker {worker + 1}", f"task {task + 1}") for worker, task in optimal_assignment_1])
print("Total Cost:", total_cost_1)
