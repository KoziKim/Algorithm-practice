from collections import deque

n, k = map(int, input().split())
graph = [[]] # 인덱스 1부터 하려고 [] 넣어놓음
check = [False for _ in range(n+1)]
for i in range(n):
    a = list(input())
    graph.append(a)

s, e = map(int, input().split())
q = deque()
q.append((graph[s], str(s))) # 경로에 시작 넣어놓음 
check[s] = True
# print(graph[s][1])

while q:
    x, hm_route = q.popleft()
    if x == graph[e]:
        print(hm_route)
        exit()
    for i in range(1, n+1):
        if check[i]:
            continue
        dist = 0
        for j in range(k):
            if x[j] != graph[i][j]:
                dist += 1
        if dist == 1:
            nx = graph[i]
            check[i] = True
            q.append((nx, hm_route + " " + str(i)))
print(-1)