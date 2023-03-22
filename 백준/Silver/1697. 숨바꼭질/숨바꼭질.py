from collections import deque
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

q = deque()
q.append(N)
MAX = 10**5
check = [0] * (MAX + 1)

while q:
    x = q.popleft()
    if x == K:
        print(check[x])
        break
    for nx in (x+1, x-1, 2*x):
        if nx < 0 or nx > MAX: 
            continue
        if check[nx] == 0:
            check[nx] = check[x] + 1
            q.append(nx)