from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
start_point = []
graph = []
ans = 1e9

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            start_point.append((i,j))

check = [[False]*n for _ in range(n)]
q = deque()
islands = set()

for i in range(len(start_point)):
    x, y = start_point[i]
    if check[x][y] == True:
        continue
    check[x][y] = True
    graph[x][y] = i + 1
    islands.add(i+1)
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if nx >= n or ny >= n or nx < 0 or ny < 0 \
                or check[nx][ny] == True or graph[nx][ny] == 0:
                continue
            check[nx][ny] = True
            graph[nx][ny] = i + 1
            islands.add(i+1)
            q.append((nx,ny))

def find_shortest_bridge(start):
    global ans

    d = deque()
    for i in range(len(start_point)):
        x, y = start_point[i]
        if graph[x][y] == start:
            d.append((x, y, 0))
        else:
            continue

    check = [[False]*n for _ in range(n)]

    while d:
        x, y, length = d.popleft()
        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if nx >= n or ny >= n or nx < 0 or ny < 0 or check[nx][ny] == True \
                or (graph[x][y] != 0 and (graph[x][y] == graph[nx][ny])):
                continue
            if graph[nx][ny] != 0 and graph[nx][ny] != start:
                ans = min(ans, length)
                return
            check[nx][ny] = True
            d.append((nx, ny, length + 1))

for island in islands:
    find_shortest_bridge(island)

print(ans)