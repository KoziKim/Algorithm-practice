a, b = map(int, input().split())

if a >= (7 * b): # 4배 2배 1배 (자신)
    print(7000*b)
elif a >= (3.5 * b): # 2배 1배(자신) 0.5배
    print(3500*b)
elif a >= (1.75 * b): # 1배(자신) 0.5배 0.25배
    print(1750 * b)
else:
    print(0)