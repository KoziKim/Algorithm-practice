import math

A, B, V = input().split()

A = int(A)
B = int(B)
V = int(V)

S = math.ceil((V - A)/(A - B)) + 1
print(S)