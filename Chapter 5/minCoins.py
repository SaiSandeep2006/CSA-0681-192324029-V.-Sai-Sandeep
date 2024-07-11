def minCoins(coins, target):
    coins.sort()
    current_sum = 0
    additions = 0
    
    for coin in coins:
        while current_sum + 1 < coin:
            current_sum += (current_sum + 1)
            additions += 1
            if current_sum >= target:
                return additions
        current_sum += coin
        if current_sum >= target:
            return additions
    
    while current_sum < target:
        current_sum += (current_sum + 1)
        additions += 1
        
    return additions


coins1 = [1, 4, 10]
target1 = 19
print("2) ",minCoins(coins1, target1)) 