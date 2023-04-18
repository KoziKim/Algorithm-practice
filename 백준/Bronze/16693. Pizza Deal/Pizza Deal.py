from math import pi
A, P1 = map(int, input().split())
R, P2 = map(int, input().split())

if A / P1 > (pi * R ** 2) / P2:
    print("Slice of pizza")
elif A / P1 < (pi * R ** 2) / P2:
    print("Whole pizza")