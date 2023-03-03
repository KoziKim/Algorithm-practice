N, M = input().split()
A = input().split()

N = int(N)
M = int(M)

A = list(map(int, A))
tmp = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if A[i] + A[j] + A[k] > M:
                continue
            elif tmp == 0:
                tmp = A[i] + A[j] + A[k]
            elif tmp < A[i] + A[j] + A[k]:
                tmp = A[i] + A[j] + A[k]

print(tmp)