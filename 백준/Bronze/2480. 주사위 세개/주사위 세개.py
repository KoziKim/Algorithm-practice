a, b, c = map(int, input().split())
A = [a, b, c]

if a == b == c:
    print(10000 + (a * 1000))
elif a == b:
    print(1000 + (a * 100))
elif a == c:
    print(1000 + (a * 100))
elif b == c:
    print(1000 + (b * 100))
else:
    A.sort()
    print(A[-1]*100)