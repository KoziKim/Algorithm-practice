a, b = map(int, input().split())

if a != b:
    print(f"Odd {2*max(a, b)}")
elif a == b == 0:
    print("Not a moose")
elif a == b:
    print(f"Even {2*a}")