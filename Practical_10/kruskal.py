# Kruskal's Algorithm

edges = [
    (2, 0, 1),
    (3, 0, 2),
    (1, 1, 2),
    (4, 1, 3),
    (2, 2, 3),
    (5, 2, 4),
    (3, 3, 4)
]

parent = [0, 1, 2, 3, 4]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

mst = []

# Sort edges by weight
edges.sort()

for weight, u, v in edges:
    pu = find(u)
    pv = find(v)

    if pu != pv:
        parent[pu] = pv
        mst.append((u, v, weight))

print("Minimum Spanning Tree:")

total = 0

for u, v, weight in mst:
    print(u, "--", v, "=", weight)
    total += weight

print("Total Cost:", total)
