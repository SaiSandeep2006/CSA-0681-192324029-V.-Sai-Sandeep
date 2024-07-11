def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0 for _ in range(n)] for _ in range(n)]
    root = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for L in range(2, n + 1):
        for i in range(n - L + 2):
            j = i + L - 1
            cost[i][j] = float('inf')
            for r in range(i, j + 1):
                c = 0 if r > i else cost[i][r - 1]
                c += 0 if r < j else cost[r + 1][j]
                c += sum(freq[i:j + 1])
                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r

    return cost[0][n - 1], root

# Test cases
keys1 = [10, 12]
freq1 = [34, 50]
keys2 = [10, 12, 20]
freq2 = [34, 8, 50]

result1, _ = optimal_bst(keys1, freq1)
result2, _ = optimal_bst(keys2, freq2)

print("Output for Test Case 1:", result1)
print("Output for Test Case 2:", result2)
