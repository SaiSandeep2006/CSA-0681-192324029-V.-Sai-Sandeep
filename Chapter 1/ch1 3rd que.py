def sum(nums):
    n = len(nums)
    t= 0
    for i in range(n):
        for j in range(i, n):
           arr = nums[i:j+1]
           dis = len(set(arr))
           t+= dis ** 2    
    return t
nums = [1, 2, 1]
print(sum(nums))