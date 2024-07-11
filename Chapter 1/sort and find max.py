def sort(arr):
    n=len(arr)-1
    if arr==[]:
        print("Array is empty")
    else:
        arr.sort()
        print(arr)
        print("Max element:",max(arr))
arr1=[2,3,1,5,4]
sort(arr1)