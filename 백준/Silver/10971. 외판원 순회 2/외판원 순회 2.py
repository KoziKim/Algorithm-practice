import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for i in range(N)]
check = [False] * N
ans = 10000000

def dfs(i, now, cost):
    global ans

    if i == N:
        if W[now][0]:
            ans = min(ans, cost + W[now][0])
        return
    for next in range(1, N):
        if W[now][next] and not check[next]:
            check[next] = True
            dfs(i+1, next, cost + W[now][next])
            check[next] = False

dfs(1, 0, 0)
print(ans)
