def median_of_medians(arr, k):
  def partition(arr, l, r, pivot_idx):
      pivot_value = arr[pivot_idx]
      arr[pivot_idx], arr[r] = arr[r], arr[pivot_idx]
      store_idx = l
      for i in range(l, r):
       if arr[i] < pivot_value:
              arr[store_idx], arr[i] = arr[i], arr[store_idx]
              store_idx += 1
      arr[store_idx], arr[r] = arr[r], arr[store_idx]
      return store_idx
  def select(arr, l, r, k):
      if l == r:
          return arr[l]
      pivot_idx = l
      while True:
          pivot_idx = partition(arr, l, r, pivot_idx)
          if pivot_idx == k:
              return arr[k]
          elif k < pivot_idx:
              r = pivot_idx - 1
          else:
              l = pivot_idx + 1
  n = len(arr)
  groups = [arr[i:i + 5] for i in range(0, n, 5)]
  medians = [sorted(group)[len(group) // 2] for group in groups]
  if len(medians) <= 5:
      pivot = sorted(medians)[len(medians) // 2]
  else:
      pivot = median_of_medians(medians, len(medians) // 2)
  pivot_idx = arr.index(pivot)
  arr[pivot_idx], arr[n - 1] = arr[n - 1], arr[pivot_idx]
  return select(arr, 0, n - 1, k)
arr = [12, 3, 5, 7, 19]
k = 2
result = median_of_medians(arr, k)
print(result)
