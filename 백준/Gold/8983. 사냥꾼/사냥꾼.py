import sys
from bisect import bisect_left 
input = sys.stdin.readline

# M = 사대의 수, N = 동물의 수, L = 사정거리
M, N, L = map(int, input().split())

# 사대 M개의 x좌표값 (정렬)
Xm = sorted(list(map(int, input().split())))

cnt = 0
for _ in range(N):
    # 동물 위치 좌표
    x, y = map(int, input().split())
    if y <= L: 
        index = bisect_left(Xm, x)
        for i in [index-1, index, index+1]:
            if i < 0 or i >= M:
                continue
            if abs(Xm[i] - x) + y <= L:
                cnt += 1
                break

print(cnt)