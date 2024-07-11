def count_ways_to_sum(num_dice, num_sides, target):
    dp = [[0] * (target + 1) for _ in range(num_dice + 1)]
    dp[0][0] = 1

    for i in range(1, num_dice + 1):
        for j in range(1, num_sides + 1):
            for k in range(j, target + 1):
                dp[i][k] += dp[i - 1][k - j]

    return dp[num_dice][target]
num_sides_1, num_dice_1, target_1 = 6, 2, 7

ways_to_sum_1 = count_ways_to_sum(num_dice_1, num_sides_1, target_1)
print(f"Number of ways to reach sum {target_1}: {ways_to_sum_1}")
