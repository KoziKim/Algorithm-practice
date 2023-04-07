from heapq import heappush, heappop
from collections import deque

N, M = map(int, input().split())

boxq = []
present_num = list(map(int, input().split()))
wish_num = list(map(int, input().split()))
wish_q = deque(wish_num)

for i in range(N):
    heappush(boxq, -present_num[i])

for i in range(M):
    max_box = -heappop(boxq)
    if max_box < wish_num[i]:
        break
    else:
        heappush(boxq, -(max_box - wish_num[i]))
        wish_q.popleft()

if wish_q:
    print(0)
else:
    print(1)