n, m = map(int, input().split())
a, b, c, d = 28, 29, 30, 31
if n - 7 == m + 7:
    print(m + 7)
elif (n-7) + a == m + 7:
    if m + 7 - a <= 0:
        print(m + 7)
    else:
        print(m + 7 - a)
elif (n-7) + b == m + 7:
    if m+7-b <=0:
        print(m + 7)
    else:
        print(m + 7 - b)
elif (n-7) + c == m + 7:
    if m + 7 - a <= 0:
        print(m + 7)
    else:
        print(m + 7 - c)
elif (n-7) + d == m + 7:
    if m + 7 - a <= 0:
        print(m + 7)
    else:
        print(m + 7 - d)