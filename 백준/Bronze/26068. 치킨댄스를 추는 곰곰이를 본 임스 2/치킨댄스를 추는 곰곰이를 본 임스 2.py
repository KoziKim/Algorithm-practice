n = int(input())

cnt = 0
for i in range(n):
    a = input()
    b = int(a[2:])
    if b <= 90:
        cnt += 1
print(cnt)