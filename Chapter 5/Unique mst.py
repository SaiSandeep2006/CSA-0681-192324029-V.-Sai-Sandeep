def is_unique_mst(n, edges, given_mst):
    def find_mst():
        uf = UnionFind(n)
        mst = []
        for u, v, weight in edges:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                mst.append((u, v, weight))
        return mst
    
    edges.sort(key=lambda x: x[2])
    given_mst_set = set(given_mst)
    
    first_mst = find_mst()
    if set(first_mst) == given_mst_set:
        return True, first_mst, None
    
    for u, v, w in first_mst:
        if (u, v, w) not in given_mst_set:
            alternate_mst = find_mst()
            return False, first_mst, alternate_mst
    
    return True, first_mst, None

n1 = 4
edges1 = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
given_mst1 = [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
unique1, mst1, another_mst1 = is_unique_mst(n1, edges1, given_mst1)
print(f"Is the given MST unique? {unique1}")