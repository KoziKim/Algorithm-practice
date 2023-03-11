import sys
input = sys.stdin.readline
N, C = map(int, input().split())
house = []
ans = 0

for i in range(N):
    house.append(int(input()))

house.sort()

start = 1
end = house[-1] - house[0]

while start <= end:
    maxlen = (start + end) // 2
    current = house[0]
    cnt = 1

    for i in range(1, len(house)):
        if house[i] >= current + maxlen:
            cnt += 1
            current = house[i]
    if cnt >= C:
        start = maxlen + 1
        ans = maxlen
    else:
        end = maxlen - 1

print(ans)