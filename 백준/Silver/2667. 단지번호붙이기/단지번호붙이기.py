from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    n = len(graph)
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append(bfs(graph, i, j))

house.sort()
print(len(house))
for i in range(len(house)):
    print(house[i])