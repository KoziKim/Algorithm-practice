import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(k):
    visited[k] = 1
    for nx in graph[k]:
        if not visited[nx]:
            dfs(nx)

cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        # if not graph[i]:
        #     cnt += 1
        #     visited[i] = 1
        # else:
            dfs(i)
            cnt += 1

print(cnt)