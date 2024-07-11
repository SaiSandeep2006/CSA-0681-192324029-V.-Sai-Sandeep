def binary_search(arr, target):
 low = 0
 high = len(arr) - 1
 while low <= high:
     mid = (low + high) // 2
     if arr[mid] == target:
         return mid
     elif arr[mid] < target:
         low = mid + 1
     else:
         high = mid - 1
 return -1
sorted_array = [3, 9, 14, 19, 25, 31, 42, 47, 53]
target_element = 31
result = binary_search(sorted_array, target_element)
print("Position of element 31 in the sorted array:", result)
