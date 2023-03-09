import sys
input = sys.stdin.readline
N = int(input())
# tmp = N
cnt = 0
tmp = N

while 1:
    cnt += 1
    new = tmp // 10 + tmp % 10
    tmp = ((tmp % 10) * 10) + new % 10
    if tmp == N:
        break

print(cnt)