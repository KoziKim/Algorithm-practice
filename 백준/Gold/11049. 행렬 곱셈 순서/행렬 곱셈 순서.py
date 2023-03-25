import sys
inp = sys.stdin.readline
N = int(inp().rstrip())

r = [0] * N
c = [0] * N
dp = [[0] * N for _ in range(N)]

def solve(x, y):
    ans = sys.maxsize
    if dp[x][y] > 0:
        return dp[x][y]
    if y - x <= 0:
        return 0
    for k in range(x, y):
        ans = min(ans, r[x]*c[k]*c[y] + solve(x, k) + solve(k+1, y))
    dp[x][y] = ans
    return dp[x][y]

for i in range(N):
    r[i], c[i] = map(int, inp().split())

print(solve(0, N-1))