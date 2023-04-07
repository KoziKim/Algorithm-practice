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
        print(0)
        break
    else:
        heappush(boxq, -(max_box - wish_num[i]))
else:
    print(1)