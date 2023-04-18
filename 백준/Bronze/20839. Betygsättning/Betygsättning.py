x, y, z = map(int, input().split())

a, c, e = map(int, input().split())

if a >= x and c >= y and e >= z:
    print("A")
elif c >= y and e >= z:
    if a >= x/2:
        print("B")
    else:
        print("C")
elif e >= z:
    if c >= y/2:
        print("D")
    else:
        print("E")