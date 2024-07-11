def canAssign(jobs, k, max_time):
    workers = [0] * k
    
    def backtrack(index):
        if index == len(jobs):
            return True
        for i in range(k):
            if workers[i] + jobs[index] <= max_time:
                workers[i] += jobs[index]
                if backtrack(index + 1):
                    return True
                workers[i] -= jobs[index]
            if workers[i] == 0:
                break
        return False
    
    jobs.sort(reverse=True)
    return backtrack(0)
def minimumTimeRequired(jobs, k):
    left, right = max(jobs), sum(jobs)
    
    while left < right:
        mid = (left + right) // 2
        if canAssign(jobs, k, mid):
            right = mid
        else:
            left = mid + 1
    
    return left

jobs1 = [3, 2, 3]
k1 = 3
print("3) ",minimumTimeRequired(jobs1, k1))  