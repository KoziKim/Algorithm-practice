from math import ceil
n, a, b, c, d = map(int, input().split())

A = b*ceil(n/a)
B = d*ceil(n/c)

if A < B:
    print(A)
else:
    print(B)