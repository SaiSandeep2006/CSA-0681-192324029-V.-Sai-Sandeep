arr=[3,1,2,2,2,1,3]
c=1
k=2
for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if arr[i]==arr[j]:
            if ((i*j)/k)==0:
                c+=1
print(c)