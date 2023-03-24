import sys

inp = sys.stdin.readline

N = int(inp())
times = []

for i in range(N):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x: x[0])
times.sort(key=lambda x: x[1])

ans = []

ans.append(times[0])

for i in range(1, N):
    if times[i][0] > times[i][1]:
        continue
    if ans[-1][1] <= times[i][0]:
        ans.append(times[i])

print(len(ans))