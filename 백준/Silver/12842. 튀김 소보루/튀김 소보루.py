import sys
from math import lcm

n, s = map(int, input().split())
m = int(input())
t = [int(sys.stdin.readline().rstrip()) for _ in range(m)]

lcm_t = lcm(*t)
total_bread_per_cycle = 0

for i in range(m):
    total_bread_per_cycle += lcm_t//t[i]

quotient = (n-s)//total_bread_per_cycle
n -= quotient*total_bread_per_cycle

if n == s:
    print(m)

cnt = 0
while n > s:
    for i in range(len(t)):
        if cnt%t[i] == 0:
            n -= 1
        if n == s:
            print(i+1)
            break
    cnt += 1