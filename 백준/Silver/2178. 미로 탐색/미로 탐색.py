from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().split())

_map = []

for i in range(N):
    _map.append(list(map(int, input().rstrip())))

def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        i, j = q.popleft()
        # 4 방향에 대해서
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            # 위치 벗어나면
            if ni < 0 or nj < 0 or ni >= N or nj >= M:
                continue
            # 0이면 갈 수 없음
            if _map[ni][nj] == 0:
                continue
            # 1이면, 이동하고 횟수 1 더해서 _map[ni][nj]에 저장
            if _map[ni][nj] == 1:
                _map[ni][nj] = _map[i][j] + 1
                q.append((ni, nj))

    return _map[N-1][M-1]

print(bfs(0, 0))