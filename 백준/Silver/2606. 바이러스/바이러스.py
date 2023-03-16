#BFS

from collections import deque

n = int(input())
k = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

Q = deque([1])

while Q:
    current = Q.popleft()
    for nx in graph[current]:
        if visited[nx] == 0:
            Q.append(nx)
            visited[nx] = 1

print(sum(visited)-1)