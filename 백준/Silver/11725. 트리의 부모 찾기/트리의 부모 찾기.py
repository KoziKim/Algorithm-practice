import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for i in range(1, N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
Q = deque([1])
visited[1] = 1
ans = [0]*(N+1)

while Q:
    now = Q.popleft()
    for i in graph[now]:
        if visited[i] == 0:
            ans[i] = now
            Q.append(i)
            visited[i] = 1

for i in range(2, N+1):
    print(ans[i])