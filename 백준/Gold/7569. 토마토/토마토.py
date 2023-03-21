from sys import stdin
from collections import deque
input = stdin.readline

M, N, H = map(int, input().split())

q = deque()
tomatos = []

for i in range(H):
    one_box = []
    for j in range(N):
        one_box += [list(map(int, input().split()))]
        for k in range(M):
            if one_box[j][k] == 1:
                q.append([i, j, k])
    tomatos.append(one_box)

while q:
    x, y, z = q.popleft()

    for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)): # 6면
        nx, ny, nz = x + dx, y + dy, z + dz
        if (0 <= nx < H) and (0 <= ny < N) and (0 <= nz < M) and tomatos[nx][ny][nz] == 0:
            tomatos[nx][ny][nz] = tomatos[x][y][z] + 1 # 일 수 더하기
            q.append([nx, ny, nz])

day = 0
for i in tomatos: # 토마토 한 상자 마다
    for j in i: # 토마토 가로 한 줄 마다
        for k in j: # 토마토 하나 마다
            if k == 0: # 안 익은 거 있으면
                print(-1)
                exit()
        day = max(day, max(j)) # 가장 많은 일수로 갱신
print(day-1) # 1(익은 상태)에서 1 더해서 저장하기 때문에 1 빼줌