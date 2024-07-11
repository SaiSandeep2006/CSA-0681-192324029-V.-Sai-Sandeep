def binary_search(arr, target):
 left, right = 0, len(arr) - 1
 comparisons = 0
 while left <= right:
     mid = left + (right - left) // 2
     comparisons += 1
     if arr[mid] == target:
         return mid, comparisons
     elif arr[mid] < target:
         left = mid + 1
     else:
         right = mid - 1
 return -1, comparisons
arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]
target = 20
index, comparisons = binary_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")
print(f"Number of comparisons made: {comparisons}")