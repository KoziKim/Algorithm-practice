import sys
from collections import deque
N = int(sys.stdin.readline())
q = deque(maxlen=2000000)

for i in range(N):
    A = sys.stdin.readline().split()
    if A[0] == "push":
        q.append(int(A[1]))
        continue
    if A[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
        continue
    if A[0] == "size":
        print(len(q))
        continue
    if A[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
        continue
    if A[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
        continue
    if A[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)