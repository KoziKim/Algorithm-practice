import sys
import heapq

input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def dijkstra():
    hq = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    heapq.heappush(hq, (0, 0, 0))

    while hq:
        weight, x, y = heapq.heappop(hq)
        if x == n-1 and y == n-1:
            return weight

        for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if graph[nx][ny] == 1: # 흰방이면
                heapq.heappush(hq, (weight, nx, ny)) # 현재 비용 그대로
            else: # 검은방이면
                heapq.heappush(hq, (weight+1, nx, ny)) # 비용 1 더함

answer = dijkstra()
print(answer)