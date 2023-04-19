a, b, c = map(int, input().split(':'))
x, y, z = map(int, input().split(':'))

if a == x and b > y:
    print(3600 * (x+24) + 60 * y + z - (3600 * a + 60 * b + c))
elif a == x and b == y and c > z:
    print(3600 * (x+24) + 60 * y + z - (3600 * a + 60 * b + c))
elif a <= x:
    print(3600 * x + 60 * y + z - (3600 * a + 60 * b + c))
else:
    print(3600 * (x+24) + 60 * y + z - (3600 * a + 60 * b + c))