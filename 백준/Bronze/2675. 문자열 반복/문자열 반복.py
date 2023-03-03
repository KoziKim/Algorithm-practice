N = int(input())
C = str()

for i in range(0, N):
    A = input().split()
    M = len(A[1])
    for j in range(0, M):
        C = C + int(A[0])*A[1][j]
        if j == M - 1:
            print(C)
            C = str()