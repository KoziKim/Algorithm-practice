a, p = map(int, input().split())

A = 7*a
P = 13*p

if A > P:
    print('Axel')
elif A < P:
    print('Petra')
else:
    print('lika')