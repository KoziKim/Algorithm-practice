import sys
input = sys.stdin.readline
N = int(input())
A = [int(input()) for i in range(N)]
S = [0]

for i in range(N-1, -1, -1):
    if A[i] > S[-1]:
        S.append(A[i])

print(len(S)-1)