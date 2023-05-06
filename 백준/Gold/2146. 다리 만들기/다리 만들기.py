from collections import deque

n = int(input())
start_point = []
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

i_num = set()

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            start_point.append((i,j))

q = deque()
ans = 1e9

check = [[False]*n for _ in range(n)]

for i in range(len(start_point)):
    x, y = start_point[i]
    if check[x][y] == True:
        continue
    check[x][y] = True
    graph[x][y] = i + 1
    i_num.add(i+1)
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
            i_num.add(i+1)
            q.append((nx,ny))

# print(graph)

def find_shortest_bridge(start):
    global ans
    check = [[False]*n for _ in range(n)]
    d = deque()
    for i in range(len(start_point)):
        x, y = start_point[i]
        if graph[x][y] == start:
            d.append((x, y, 0))
        else:
            continue
    # for i in range(n):
    #     for j in range(n):
    #         if graph[i][j] == start:
    #             q.append((i, j, 0))

    check = [[False]*n for _ in range(n)]

    while d:
        x, y, length = d.popleft()
        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if nx >= n or ny >= n or nx < 0 or ny < 0 \
                or check[nx][ny] == True \
                or (graph[x][y] != 0 and (graph[x][y] == graph[nx][ny])):
                continue
            if graph[nx][ny] != 0 and graph[nx][ny] != start:
                ans = min(ans, length)
                return

            check[nx][ny] = True
            d.append((nx, ny, length + 1))

for num in i_num:
    find_shortest_bridge(num)

print(ans)