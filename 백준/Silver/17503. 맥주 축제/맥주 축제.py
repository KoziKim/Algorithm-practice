import sys
from heapq import heappop, heappush

# n 축제 열리는 기간, 선호도 합 m, 마실 수 있는 맥주 종류 수 k

n, m, k = map(int, input().split())

# k개 줄, 선호도 v 도수 레벨 c
beers = []

sum_v = 0
for i in range(k):
    v, c = map(int, sys.stdin.readline().split())
    beers.append([v, c])
beers.sort(key=lambda x: x[1])

candi = []

for i in range(k):
    v, c = beers[i]
    heappush(candi, (v, c))
    sum_v += v
    if len(candi) == n:
        if sum_v >= m:
            print(c)
            exit()
        else:
            sum_v -= heappop(candi)[0]
else:
    print(-1)