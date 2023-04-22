from collections import deque

n, k = map(int, input().split())
graph = [[]] # 인덱스 1부터 하려고 [] 넣어놓음
check = [False for _ in range(n+1)]
for i in range(n):
    a = list(input())
    graph.append(a)

s, e = map(int, input().split())
q = deque()
q.append((s, str(s))) # 경로에 시작 넣어놓음 
check[s] = True

while q:
    start, hm_route = q.popleft()
    if start == e:
        print(hm_route)
        exit()
    for i in range(1, n+1):
        dist = 0
        for j in range(k):
            if graph[start][j] != graph[i][j]:
                dist += 1
        if dist == 1 and not check[i]:
            check[i] = True
            q.append((i, hm_route + " " + str(i)))
print(-1)