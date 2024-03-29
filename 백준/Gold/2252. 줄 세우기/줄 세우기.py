import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
inDegree = [0 for i in range(n+1)]
graph = [[] for i in range(n+1)]
q = deque()
ans = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, n + 1):
    if inDegree[i] == 0:
        q.append(i)

while q:
    student = q.popleft()
    ans.append(student)
    for j in graph[student]:
        inDegree[j] -= 1
        if inDegree[j] == 0:
            q.append(j)

print(*ans)