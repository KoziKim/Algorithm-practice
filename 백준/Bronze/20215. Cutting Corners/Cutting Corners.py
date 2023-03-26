a, b = map(int, input().split())

if (a**2 + b**2)**(1/2) == int((a**2 + b**2)**(1/2)):
    print(a + b - int((a**2 + b**2)**(1/2)))
else:
    print(f"{a + b - ((a**2 + b**2)**(1/2)):.10f}")