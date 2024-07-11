def brute(points):
    mini= float('inf')
    closest= None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1 = points[i]
            p2 = points[j]
            dis = distance(p1, p2)            
            if dis < mini:
                mini = dis
                closest = (p1, p2)                
    return closest, mini
def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
point = [(0, 0), (1, 1), (4, 5), (3, 1)]
res , value = brute(point)
print(res)
print(value)