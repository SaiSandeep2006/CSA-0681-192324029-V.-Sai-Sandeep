arr=[3,7,3,5,2,5,9,2]
temp=[]
for x in arr:
    if x not in temp:
        temp.append(x)
print(temp)