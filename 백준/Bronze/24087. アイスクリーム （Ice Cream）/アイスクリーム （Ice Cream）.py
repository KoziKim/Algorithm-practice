from math import ceil

S = int(input())
A = int(input())
B = int(input())

if S <= A:
    print(250)
else:
    print(250 + 100 * ceil((S - A)/B))