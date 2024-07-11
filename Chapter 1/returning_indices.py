arr1=[2,3,2]
arr2=[1,2]
for i in range(0,len(arr1)):
    for j in range(0,len(arr2)):
        if arr1[i]==arr2[j]:
            print(i,j)