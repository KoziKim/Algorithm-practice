n = int(input())
a, b = map(int, input().split())
cnt = 0
while n > 0:
    while a > 1:
        a -= 2
        n -= 1
        cnt += 1
        if n == 0:
            break
    while b > 0 and n > 0:
        b -= 1
        n -= 1
        cnt += 1
        if n == 0:
            break
    n -= 1
print(cnt)