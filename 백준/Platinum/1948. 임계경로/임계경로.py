import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
back = [[] for _ in range(N+1)]

for _ in range(M):
    # a: 출발 도시, b: 도착 도시, c: 걸리는 시간
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    indegree[b] += 1

start, end = map(int, input().split())

q = deque([])
q.append(start)

time = [0] * (N+1)

while q:
    # now: 도시, back: 직전 경로(경로 추적 위함)
    now = q.popleft()

    for (next, cost) in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)
        if time[next] < time[now] + cost:
            # 더 오래 걸리는 걸로 갱신
            time[next] = time[now] + cost
            # 직전 경로도 갱신
            back[next] = [now]
        # 시간이 같을 경우(같은 시간 경로 여러개일 경우), 추가함.
        elif time[next] == time[now] + cost:
            back[next].append(now)

q = deque([end])
route = set()
while q:
    now = q.popleft()
    for nx in back[now]:
        if (now, nx) not in route:
            route.add((now, nx))
            q.append(nx)

print(time[end])
print(len(route))