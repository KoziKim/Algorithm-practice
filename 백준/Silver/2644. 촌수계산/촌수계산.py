from collections import deque

n = int(input())
a, b = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n+1)]
check = [False for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque()
q.append((a, 0))
f = 0
while q:
    me, chon = q.popleft()
    for person in graph[me]:
        if check[person] == True:
            continue
        if check[person] == False:
            check[person] = True
            q.append((person, chon + 1))
        if person == b:
            print(chon + 1)
            f = 1
            break
    if f == 1:
        break
else:
    print(-1)