N = int(input())
time = []

for i in range(N):
    a, b = map(int, input().split())
    if a <= b:
        time.append(b)
if time:
    print(min(time))
else:
    print(-1)