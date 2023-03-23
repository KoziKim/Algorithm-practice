while True:
    A = int(input())
    _sum = 0
    if A == 0:
        exit()
    for i in range(A):
        _sum += A - i
    print(_sum)