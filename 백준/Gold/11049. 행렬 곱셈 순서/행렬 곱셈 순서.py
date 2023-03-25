import sys
input = sys.stdin.readline

N = int(input())

A = []
for _ in range(N):
  a, b = map(int, input().split())
  A.append(a)
A.append(b)

min_mult = [ [0]*(N+1) for _ in range(N+1) ]

for i in range(N, -1, -1):
  for j in range(i+2, N+1):
    min_mult[i][j] = min([A[i]*A[k]*A[j] + min_mult[i][k] + min_mult[k][j] for k in range(i+1, j)])

print(min_mult[0][N])