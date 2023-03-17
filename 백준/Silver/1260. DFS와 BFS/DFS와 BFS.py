from collections import deque
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    if len(graph[i]) == 1:
        continue
    if graph[i]:
        graph[i].sort() 

def dfs(k):
    print(k, end = ' ')
    visited[k] = 1
    for nx in graph[k]:
        if visited[nx] == 0:
            dfs(nx)

dfs(V)
print()

visited = [0] * (N+1)
Q = deque([V])
visited[V] = 1

while Q:
    current = Q.popleft()
    print(current, end = ' ')
    for nx in graph[current]:
        if visited[nx] == 0:
            Q.append(nx)
            visited[nx] = 1