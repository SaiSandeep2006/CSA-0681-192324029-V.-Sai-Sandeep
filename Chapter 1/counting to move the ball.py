def number(m, n, N, i, j):
    dict = {}
    if i < 0 or i >= m or j < 0 or j >= n:
        return 1
    if N == 0:
        return 0
    if (N, i, j) in dict:
        return dict[(steps, i, j)]   
    ways = 0
    for i in range (m*n):
         ways += number(m, n, N - 1, i - 1, j)    
         dict[(N, i, j)] = ways
    return ways
m = 2
n = 2
N = 2
srow = 0
scol = 0
ways = number(m, n, N, srow, scol)
print("Number of ways to move the ball out of the grid in exactly N steps:", ways)