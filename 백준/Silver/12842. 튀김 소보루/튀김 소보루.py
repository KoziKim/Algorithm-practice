import sys
from math import lcm

n, s = map(int, input().split())

m = int(input())

t = []

cnt = 0

for i in range(m):
    t.append(int(sys.stdin.readline().rstrip()))

lcm_t = lcm(*t)

yeah = 0
for i in range(m):
    yeah += lcm_t//t[i]

k = n-s

a = k//yeah

n -= a*yeah

if n == s:
    print(m)

while n > s:
    for i in range(len(t)):
        if cnt%t[i] == 0:
            n -= 1
        if n == s:
            print(i+1)
            break
    if n == s:
        break
    cnt += 1