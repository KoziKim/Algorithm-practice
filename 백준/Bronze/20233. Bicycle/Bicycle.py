a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

if T >= 45:
    print(a + 21*(T - 30)*x, b + 21*(T - 45)*y)
elif T >= 30:
    print(a + 21*(T-30)*x, b)
else:
    print(a, b)