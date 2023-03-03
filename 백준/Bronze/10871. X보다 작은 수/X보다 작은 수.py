N, X = input().split()
A = input().split()

N = int(N)
X = int(X)
B = []
C = str()
k = 0

for i in range (0, N):
    if int(A[i]) < X:
        B.append(A[i])
        k = k + 1

for j in range(0, k):
    if j != k-1:
        C = C + B[j] + " "
    else:
        C = C + B[j]

print(C)