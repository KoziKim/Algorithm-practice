import sys

inp = sys.stdin.readline

T = int(inp())

for _ in range(T):
    N = int(inp())
    coins = list(map(int, inp().split()))
    M = int(inp())
    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, M+1):
            dp[i] += dp[i-coin]
    print(dp[M])