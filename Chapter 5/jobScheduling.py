from bisect import bisect_left

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    dp = [(0, 0)]  
    for s, e, p in jobs:
        i = bisect_left(dp, (s,))
        if dp[i-1][1] + p > dp[-1][1]:
            dp.append((e, dp[i-1][1] + p))
    
    return dp[-1][1]


startTime1 = [1, 2, 3, 3]
endTime1 = [3, 4, 5, 6]
profit1 = [50, 10, 40, 70]
print("4) ",jobScheduling(startTime1, endTime1, profit1))  