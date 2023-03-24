import sys

inp = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(inp()))

cnt = 0

for i in coins[::-1]:
    if K >= i:
        cnt += K // i
        K %= i

print(cnt)