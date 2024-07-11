def tower(poured, row, glass):
    dp = [[0.0] * (r + 1) for r in range(row + 1)]
    dp[0][0] = poured  
    for i in range(row):
        for j in range(len(dp[i])):
            excess = (dp[i][j] - 1.0) / 2.0
            if excess > 0:
                dp[i + 1][j] += excess
                dp[i + 1][j + 1] += excess    
    return dp[row][glass]
poured = 2
row = 1
glass = 1
print(tower(poured, row, glass)) 