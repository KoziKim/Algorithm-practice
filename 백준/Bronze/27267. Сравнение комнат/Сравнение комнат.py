a, b, c, d = map(int, input().split())

ca = a*b
pe = c*d

if ca > pe:
    print('M')
elif ca < pe:
    print('P')
else:
    print('E')