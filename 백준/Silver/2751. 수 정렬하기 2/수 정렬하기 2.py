import sys

N = int(sys.stdin.readline())
B = []

for i in range(N):
    A = int(sys.stdin.readline())
    B.append(A)

B.sort()

for i in range(N):
    print(B[i])