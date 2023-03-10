import sys
input = sys.stdin.readline
N = int(input())
S = []

for i in range(N):
    A = int(input())
    if A == 0:
        S.pop()
    else:
        S.append(A)

print(sum(S[i] for i in range(len(S))))