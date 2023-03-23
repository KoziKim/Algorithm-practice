import sys

inp = sys.stdin.readline

n = int(inp())

d = [0] * (1000001)
d[1] = 1
d[2] = 2

def tile(n):
    for x in range(3, n+1):
        d[x] = (d[x-1] + d[x-2])%15746
    return d[n]

print(tile(n))
