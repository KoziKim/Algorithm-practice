import sys

inp = sys.stdin.readline

n = int(inp())

d = [0] * 91
d[1] = 1
d[2] = 1

def fibo(n):
    for x in range(3, n+1):
        d[x] = d[x-1] + d[x-2]
    return d[n]

print(fibo(n))