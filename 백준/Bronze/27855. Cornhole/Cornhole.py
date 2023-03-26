H1, B1 = map(int, input().split())
H2, B2 = map(int, input().split())
if (3*H1 + 1*B1) > (3*H2 + 1*B2):
    print(1, 3*H1 + 1*B1 - (3*H2 + 1*B2))
elif (3*H1 + 1*B1) < (3*H2 + 1*B2):
    print(2, 3*H2 + 1*B2 - (3*H1 + 1*B1))
else:
    print("NO SCORE")