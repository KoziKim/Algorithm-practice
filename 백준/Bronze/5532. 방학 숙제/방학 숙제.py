L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

for i in range(L-1, -1, -1):
    A -= C
    B -= D
    if A <= 0 and B <= 0:
        print(i)
        break