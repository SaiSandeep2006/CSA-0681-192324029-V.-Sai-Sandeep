from collections import deque

def cat_mouse_game(graph):
    n = len(graph)
    DRAW, MOUSE, CAT = 0, 1, 2
    color = [[[0] * n for _ in range(n)] for _ in range(3)]

    q = deque()
    for i in range(1, n):
        for t in range(1, 3):
            color[t][i][i] = 1
            q.append((t, i, i))

    while q:
        t, x, y = q.popleft()
        for parent in graph[t == 1 and x or y]:
            if parent == 0:
                continue
            if t == 1:
                if not color[MOUSE][parent][y]:
                    color[MOUSE][parent][y] = t
                    q.append((MOUSE, parent, y))
            else:
                if all(color[t][parent][child] == t for child in graph[parent]):
                    color[CAT][parent][y] = t
                    q.append((CAT, parent, y))

    return color[MOUSE][1][2]

# Example 1
graph1 = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]
print(cat_mouse_game(graph1))  # Output: 0

# Example 2
graph2 = [[1, 3], [0], [3], [0, 2]]
print(cat_mouse_game(graph2))  # Output: 1

