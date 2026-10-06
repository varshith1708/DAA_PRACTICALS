import time

# Number of vertices
n = int(input("Enter number of vertices: "))

# Number of edges
e = int(input("Enter number of edges: "))

graph = []

print("Enter edges (source destination weight):")

for i in range(e):
    u, v, w = map(int, input().split())
    graph.append([w, u, v])

# Start execution time
start_time = time.perf_counter()

# Sort edges by weight
graph.sort()

parent = list(range(n))
mst = []
total = 0

# Find parent
def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

# Prim's Algorithm
for w, u, v in graph:
    pu = find(u)
    pv = find(v)

    if pu != pv:
        parent[pu] = pv
        mst.append((u, v, w))
        total += w

        if len(mst) == n - 1:
            break

end_time = time.perf_counter()

# Output
print("\nMinimum Spanning Tree:")

for u, v, w in mst:
    print(u, "--", v, "=", w)

print("Total Cost:", total)

print("\nExecution Time:",
      end_time - start_time, "seconds")

print("Time Complexity: O(E log E)")
print("Space Complexity: O(V + E)")
