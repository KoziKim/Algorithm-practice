from math import ceil

n, t = map(int, input().split())
m = int(input())
x, y = map(int, input().split())

if t >= m / (x*60) + (n - m) / (y*60):
    print(0)
else:
    print(ceil((m / (x*60) + (n - m) / (y*60)))-t)