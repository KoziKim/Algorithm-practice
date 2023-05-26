import sys
inp = sys.stdin.readline

n, t = map(int, inp().split())

dp = [0] * (t+1)
for i in range(n):
    k, s = map(int, inp().split())
    for j in range(t, -1, -1):
        if j >= k:
            dp[j] = max(dp[j], dp[j-k] + s)

print(dp[t])