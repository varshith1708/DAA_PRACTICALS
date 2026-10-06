import time

# Graph input
n = int(input("Enter number of vertices: "))
graph = [[] for _ in range(n)]

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = map(int, input("Enter edge (u v): ").split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))


# DFS
def dfs(v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)


# BFS
def bfs(start):
    visited = [False] * n
    queue = [start]
    visited[start] = True

    while queue:
        v = queue.pop(0)
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


# DFS execution
print("\nDFS Traversal:")
visited = [False] * n

t1 = time.perf_counter()
dfs(start, visited)
t2 = time.perf_counter()

print("\nDFS Execution Time:", t2 - t1, "seconds")


# BFS execution
print("\nBFS Traversal:")

t1 = time.perf_counter()
bfs(start)
t2 = time.perf_counter()

print("\nBFS Execution Time:", t2 - t1, "seconds")


# Complexity
print("\nTime Complexity of DFS: O(V + E)")
print("Time Complexity of BFS: O(V + E)")
print("Space Complexity of DFS: O(V)")
print("Space Complexity of BFS: O(V)")
