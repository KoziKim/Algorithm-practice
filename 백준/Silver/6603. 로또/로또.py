from itertools import combinations as com

import sys
input = sys.stdin.readline
N = 1000000000

for i in range(N):
    A = input().split()
    B = []
    if A[0] == "0":
        break
    for j in range(1, len(A)):
        B.append(A[j])
    C = list(com(B, 6))
    for k in range(len(C)):
        print(' '.join(C[k]))
        if k == len(C) - 1:
            print('')