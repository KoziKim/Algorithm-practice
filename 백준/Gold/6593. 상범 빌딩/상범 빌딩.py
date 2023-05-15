from collections import deque
# l, r, c 층 행 열

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# graph = []
def bfs(i, j, k):
    check = [[[False]*c for _ in range(r)] for __ in range(l)]
    # print(check)
    q = deque()
    cnt = 0
    q.append((i, j, k, cnt))
    check[i][j][k] = True
    while q:
        x, y, z, cnt = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            # print(nx, ny, nz)
            # print(graph[0][0][0])
            if nx >= l or ny >= r or nz >= c or nx < 0 or ny < 0 or nz < 0:
                continue
            if check[nx][ny][nz] == True:
                continue
            if graph[nx][ny][nz] == "#":
                continue
            if graph[nx][ny][nz] == "E":
                print(f"Escaped in {cnt+1} minute(s).")
                return
            if graph[nx][ny][nz] == ".":
                check[nx][ny][nz] = True
                q.append((nx, ny, nz, cnt+1))
    print("Trapped!")
    return

            
candi = []

while True:
    l, r, c = map(int, input().split())
    if l == r == c == 0:
        break
    graph = [[] for _ in range(l)]
    for i in range(l):
        for j in range(r):
            line = list(input())
            graph[i].append(line)
            for k in range(c):
                if graph[i][j][k] == 'S':
                    candi.append((i, j, k))
        input()
    x, y, z = candi.pop()
    bfs(x, y, z)

    # print(graph)

# q = deque()
