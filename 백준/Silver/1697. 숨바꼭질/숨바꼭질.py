from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

q = deque()
q.append(N)
limit = 10**5
check = [0] * (limit + 1)

while q:
    x = q.popleft()
    if x == K:
        print(check[x])
        break
    for nx in (x+1, x-1, 2*x):
        if nx < 0 or nx > limit: 
            continue
        if check[nx] == 0:
            check[nx] = check[x] + 1
            q.append(nx)
