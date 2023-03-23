from collections import deque
from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
graph = []
tmp_q = []

def bfs(tmp_q, S, X, Y):
    q = deque(tmp_q)
    time = 0

    while q:
        virus, x, y, time = q.popleft()
        if time == S:
            print(graph[X-1][Y-1])
            exit()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N or graph[nx][ny] != 0:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, nx, ny, time + 1))

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            tmp_q.append((graph[i][j], i, j, 0))

tmp_q.sort()
S, X, Y = map(int, input().split())

bfs(tmp_q, S, X, Y)

print(graph[X-1][Y-1])