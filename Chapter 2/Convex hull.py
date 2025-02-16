def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2
def convex_hull(points):
    n = len(points)
    if n < 3:
        return points
    hull = []
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == l:
            break
    return hull
# Input Points
points = [(1, 1), (4, 6), (8, 1), (0, 0), (3, 3)]
# Finding Convex Hull
convex_hull_points = convex_hull(points)
# Output Convex Hull Points
print("Convex Hull:", convex_hull_points)
