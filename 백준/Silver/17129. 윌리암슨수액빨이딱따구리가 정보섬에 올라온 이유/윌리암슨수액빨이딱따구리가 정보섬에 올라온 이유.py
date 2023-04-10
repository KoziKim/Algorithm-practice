import sys
from collections import deque
inp = sys.stdin.readline
n, m = map(int, input().split())

graph = []
q = deque()

for i in range(n):
    a = inp().rstrip()
    line = []
    for j in range(m):
        line.append(int(a[j]))
        if int(a[j]) == 2:
            q.append((i,j,0))
    graph.append(line)

ans = 1e9
while q:
    x, y, cnt = q.popleft()
    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx > n-1 or ny > m-1 or graph[nx][ny] == 1:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            q.append((nx, ny, cnt+1))
            continue
        if (3 <= graph[nx][ny] <= 5):
            ans = cnt+1
            print('TAK')
            print(ans)
            exit()
else:
    print('NIE')