import sys

N = int(sys.stdin.readline())
A = []
B = []


for i in range(N):
    A.append(sys.stdin.readline().rstrip())

A = list(set(A))

A.sort()

for i in range(50):
    for j in range(len(A)):
        if len(A[j]) == i+1:
            print(A[j])
            A[j] = "a"*51