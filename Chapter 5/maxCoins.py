def maxCoins(piles):
    piles.sort(reverse=True)
    max_coins = 0
    n = len(piles) // 3 
    for i in range(n):
        max_coins += piles[2 * i + 1]
    
    return max_coins

piles1 = [2, 4, 1, 2, 7, 8]
print(maxCoins(piles1))  