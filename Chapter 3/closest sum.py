from itertools import chain, combinations
def subsets(arr):
    return chain(*[combinations(arr, i) for i in range(len(arr)+1)])
def closest_sum_subset(arr, target):
    n = len(arr)
    half = n // 2
    left_half = list(subsets(arr[:half]))
    right_half = list(subsets(arr[half:]))
    left_half_sums = [sum(subset) for subset in left_half]
    right_half_sums = [sum(subset) for subset in right_half]
    left_half_sums.sort()
    right_half_sums.sort()
    closest_sum = float('inf')
    closest_subset = None   
    i = 0
    j = len(right_half_sums) - 1    
    while i < len(left_half_sums) and j >= 0:
     current_sum = left_half_sums[i] + right_half_sums[j]     
     if abs(target - current_sum) < abs(target - closest_sum):
             closest_sum = current_sum
             closest_subset = left_half[i] + right_half[j]
             if current_sum > target:
                 j -= 1
             else:
                 i += 1    
    return closest_subset
arr = [45, 34, 4, 12, 5, 2]
target_sum = 42
result = closest_sum_subset(arr, target_sum)
print(result)
