import sys

N = int(sys.stdin.readline())
A = [0]*10000

for i in range(N):
    x = int(sys.stdin.readline())
    A[x-1] += 1

for i in range(10000):
    if A[i] != 0:
        for j in range(A[i]):
            print(i+1)