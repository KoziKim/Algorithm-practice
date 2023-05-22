n, l = map(int, input().split())

leak = list(map(int, input().split()))

leak.sort()

a = leak[0] - 0.5 + l
cnt = 1

for i in range(n):
    if a > leak[i]:
        continue
    a = leak[i] - 0.5 + l
    cnt+=1
print(cnt)
