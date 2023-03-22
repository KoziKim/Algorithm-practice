import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
return_graph = [[] for _ in range(N+1)]
cnt = [[] for _ in range(N+1)]

for _ in range(M):
    # a: 출발 도시, b: 도착 도시, c: 걸리는 시간
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    return_graph[b].append(a)
    indegree[b] += 1

start, end = map(int, input().split())

q = deque([])
q.append(start)

time = [0] * (N+1)

while q:
    # now: 도시, c: 지나온 경로의 개수
    now = q.popleft()

    for (city, cost) in graph[now]:
        indegree[city] -= 1
        # 비용이 갱신 될 때
        if time[city] < time[now] + cost:
            time[city] = time[now] + cost
            # 달려야 하는 도로의 수 갱신
            cnt[city] = [now]
        elif time[city] == time[now] + cost:
            cnt[city].append(now)

        # 선행 도로를 모두 지나갔을 때
        if indegree[city] == 0:
            q.append(city)

q = deque([end])
route = set()
while q:
    now = q.popleft()
    for x in cnt[now]:
        if (now, x) not in route:
            route.add((now, x))
            q.append(x)

print(time[end])
print(len(route))