def findKthPositive(arr, k):
    missing_count = 0
    for i in range(1, arr[-1] + 1):
        if i not in arr:
            missing_count += 1
            if missing_count == k:
                return i
    return arr[-1] + k