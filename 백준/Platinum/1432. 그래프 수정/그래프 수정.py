from heapq import *
import sys
input = sys.stdin.readline

def topology_sort(N):
    q = []
    for i in range(1, N+1):
        if degree[i] == 0:
            heappush(q, -i)

    while q:
        now = -heappop(q)
        ans[now] = N
        for i in graph[now]:
            degree[i] -= 1
            if degree[i] == 0:
                heappush(q, -i)
        N -= 1

N = int(input())
graph = [[] for _ in range((N+1))]
degree = [0] * (N+1)
ans = [0] * (N+1)

for v in range(1, N+1):
    tmp = [0] + list(map(int, input().strip()))
    for i in range(1, N+1):
        if tmp[i] == 1:
            graph[i].append(v)
            degree[v] += 1

topology_sort(N)

if ans.count(0) > 1:
    print(-1)
else:
    print(*ans[1:])
