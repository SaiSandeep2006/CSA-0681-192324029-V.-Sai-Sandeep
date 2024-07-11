def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0 for _ in range(n)] for _ in range(n)]
    root = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i

    for L in range(2, n + 1):
        for i in range(n - L + 2):
            j = i + L - 1
            cost[i][j] = float('inf')
            for r in range(i, j + 1):
                c = cost[i][r - 1] if r > i else 0
                c += cost[r + 1][j] if r < j else 0
                c += sum(freq[i:j + 1])
                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r

    return cost, root

# Test with keys A, B, C, D and frequencies 0.1, 0.2, 0.4, 0.3
keys = ['A', 'B', 'C', 'D']
freq = [0.1, 0.2, 0.4, 0.3]
cost_table, root_table = optimal_bst(keys, freq)

# Display the resulting OBST and its cost
print("Cost Table:")
for row in cost_table:
    print("\t".join(str(cost) for cost in row))

print("\nRoot Table:")
for row in root_table:
    print("\t".join(str(root) for root in row))
