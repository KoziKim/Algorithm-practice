from sys import *
from collections import deque
input = stdin.readline

N, M = map(int, input().split())

def bfs(i, j, visited):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if not visited[ni][nj] and ice[ni][nj]:
                q.append((ni,nj))
                visited[ni][nj] = 1

def solve():
    for year in range(1, 900000):
        melting = [[0] * M for _ in range(N)]
        # 0 개수 세기
        for i in range(1, N-1):
            for j in range(1, M-1):
                if not ice[i][j]:
                    continue
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if not ice[ni][nj]:
                        melting[i][j] += 1
        # 높이 낮추기
        for i in range(1, N-1):
            for j in range(1, M-1):
                if melting[i][j] > 0:
                    ice[i][j] = max(0, ice[i][j] - melting[i][j])
        # 덩어리 세기
        visited = [[0] * M for _ in range(N)]
        cnt = 0
        for i in range(1, N-1):
            for j in range(1, M-1):
                if not visited[i][j] and ice[i][j]:
                    bfs(i, j, visited)
                    cnt += 1
                    if cnt > 1:
                        return year
        if cnt == 0:
            return 0
    return -1

ice = [list(map(int, input().split())) for _ in range(N)]

ans = solve()
print(ans)