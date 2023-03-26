n = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in A:
    if i == n:
        cnt += 1
print(cnt)