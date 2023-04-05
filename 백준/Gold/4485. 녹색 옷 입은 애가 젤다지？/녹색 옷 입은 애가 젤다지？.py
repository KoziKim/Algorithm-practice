from collections import deque

num = 1

def bfs(n):
    q = deque()
    q.append((0, 0, graph[0][0]))
    while q:
        x, y, cost = q.popleft()
        if x == N-1 and y == N-1:
            continue
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x+dx, y+dy
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue
            if dp[nx][ny] <= cost + graph[nx][ny]:
                continue
            dp[nx][ny] = cost + graph[nx][ny]
            q.append((nx, ny, cost + graph[nx][ny]))
    return

while True:
    N = int(input())
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    dp = [[1e9]*N for _ in range(N)]
    bfs(N)
    print("Problem ", num, ": ", dp[N-1][N-1], sep='')
    num += 1