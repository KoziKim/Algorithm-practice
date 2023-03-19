from sys import stdin

def dfs(arr, n):
    cnt = 0
    for i in arr[n]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            cnt += dfs(arr, i)
    return cnt

N, M = map(int, stdin.readline().split())
heavier = [[] for _ in range(N+1)]  # 무거운 구슬
lighter = [[] for _ in range(N+1)]  # 가벼운 구슬
mid = (N+1) // 2  # 개수 기준 중간값

for i in range(M):
    a, b = map(int, stdin.readline().split())
    heavier[b].append(a)
    lighter[a].append(b)

answer = 0
for i in range(1, N+1):
    visited = [False] * (N+1)
    cnt = dfs(heavier, i)
    if cnt >= mid:
        answer += 1
    visited = [False] * (N+1)
    cnt = dfs(lighter, i)
    if cnt >= mid:
        answer += 1

print(answer)
