# DFS

n = int(input())
k = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(k):
    visited[k] = 1
    for nx in graph[k]:
        if visited[nx] == 0:
            dfs(nx)

dfs(1)
print(sum(visited)-1)