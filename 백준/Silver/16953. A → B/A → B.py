from collections import deque

A, B = map(int, input().split())

q = deque([(A, 1)])

if A == B:
    print(1)
    exit()

f = 0
while q:
    x, cnt = q.popleft()
    if not q and 2*x > B and (10*x + 1) > B:
        print(-1)
        break
    for dx in (x, (9*x + 1)):
        nx = x + dx
        if nx > B:
            continue
        if nx == B:
            cnt += 1
            print(cnt)
            f = 1
            break
        q.append((nx, cnt + 1))
    if f == 1:
        break