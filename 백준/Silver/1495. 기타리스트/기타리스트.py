from collections import deque
# N = 곡 수, S = 시작 볼륨, M = 최대 볼륨
N, S, M = map(int, input().split())

# 볼륨의 차이
V = list(map(int, input().split()))
dp = [set() for _ in range(N)]

# 현재 볼륨 P라면 i번 곡은 V - V[i] 또는 V + V[i] 로 연주해야 됨.
result = -1
q = deque()
q.append((S, 0))

while q:
    P, idx = q.popleft()

    if idx < len(V):
        for change in (V[idx], -V[idx]):
            newP = P + change
            if newP < 0 or newP > M:
                continue
            if newP not in dp[idx]:
                dp[idx].add(newP)
                q.append((newP, idx + 1))
    else:
        result = max(result, P)

print(result)