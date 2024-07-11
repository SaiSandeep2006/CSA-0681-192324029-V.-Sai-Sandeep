import heapq

def kClosest(points, k):
 heap = []
 for x, y in points:
     dist = -(x*x + y*y)
     if len(heap) == k:
        heapq.heappushpop(heap, (dist, x, y))
     else:
         heapq.heappush(heap, (dist, x, y))
 return [(x, y) for (dist, x, y) in heap]
 
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
print(kClosest(points, k))
