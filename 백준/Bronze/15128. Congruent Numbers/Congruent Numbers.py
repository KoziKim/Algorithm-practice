p, q, p2, q2 = map(int, input().split())
a = (1/2) * p * p2 / q / q2
if a == int(a):
    print(1)
else:
    print(0)