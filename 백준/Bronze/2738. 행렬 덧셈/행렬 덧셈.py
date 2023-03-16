N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

C = [[] for _ in range(N)]

for i in range(N):
    for j in range(M):
        C[i].append(A[i][j]+B[i][j])

for i in range(N):
    if i == N-1:
        print(*C[i], sep = ' ', end = '')
        break
    print(*C[i])