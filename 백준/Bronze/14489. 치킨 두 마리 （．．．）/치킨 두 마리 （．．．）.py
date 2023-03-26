a, b = map(int, input().split())
chi = int(input())
if (a+b) >= 2*chi:
    print(a+b - 2*chi)
else:
    print(a+b)