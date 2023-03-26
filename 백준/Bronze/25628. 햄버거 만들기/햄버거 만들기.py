b, p = map(int, input().split())
cnt = 0
while True:
    b -= 1
    p -= 1
    b -= 1
    if b >=0 and p >= 0:
        cnt += 1
    if b < 2 or p < 1:
        break
print(cnt)