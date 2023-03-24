import sys

inp = sys.stdin.readline

word1 = list(input().rstrip())
word2 = list(input().rstrip())

n = len(word1)
m = len(word2)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        if word1[i] == word2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n-1][m-1])