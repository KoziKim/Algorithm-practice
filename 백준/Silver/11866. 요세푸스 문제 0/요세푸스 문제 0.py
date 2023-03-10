import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
q = deque()
ans = []

for i in range(N):
    q.append(i+1)

i = 0

while q:
    q.append(q.popleft())
    i += 1
    if i%K == 0:
        ans.append(q.pop())
        
print("<", end = '')
print(*ans, sep = ', ', end = '')
print(">")