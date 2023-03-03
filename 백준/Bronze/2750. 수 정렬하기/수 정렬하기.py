N = int(input())
A = []

for i in range(N):
    A.append(input())
A = list(map(int, A))
A.sort()

for i in range(N):
    print(A[i])