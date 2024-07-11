def isort(arr):
  for i in range(0,len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j = j - 1
    arr[j + 1] = key
  return arr
arr = list(map(int,input().split()))
print(isort(arr))