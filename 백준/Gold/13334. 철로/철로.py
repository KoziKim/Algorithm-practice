import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
lines_init = [list(map(int, input().split())) for i in range(N)]
d = int(input())

ans = 0
lines = []
heap = []

for line in lines_init:
    h, o = line
    if abs(h - o) <= d: #하우스 <-> 오피스 간 거리가 d보다 작다면
        lines.append(sorted(line)) # 작은 숫자가 앞에 가게 해서 lines에 집어넣음.

lines.sort(key=lambda x:x[1]) # 오른쪽 수(큰 수) 기준으로 정렬함.

for line in lines:
    # 힙 최솟값이 line의 오른쪽 숫자에서 d를 뺀 것보다 작을 때
    # 즉, line의 오른쪽 끝에서 d 선로를 깐 범위를 벗어났을 때, 
    # 제외시킨다.
    while heap and heap[0][0] < line[1] - d:
        heappop(heap)
    heappush(heap, line)
    # heap이 그전 heap보다 내용물이 많으면,
    # 선로 안에 더 많은 선분이 들어있는 것이므로 정답으로 업데이트 해준다.
    ans = max(ans, len(heap))

print(ans)