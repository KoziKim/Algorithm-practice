import heapq
from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
t_cost = [1e9] * (N + 1)

for _ in range(M):
    now, next, cost = map(int, input().split())
    graph[now].append((cost, next))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    t_cost[start] = 0

    while q:
        cost, node = heapq.heappop(q)

        if t_cost[node] < cost:
            continue

        for n_cost, n_node in graph[node]:
            n_cost += cost

            if t_cost[n_node] > n_cost:
                heapq.heappush(q, (n_cost, n_node))
                t_cost[n_node] = n_cost


dijkstra(start)

print(t_cost[end])