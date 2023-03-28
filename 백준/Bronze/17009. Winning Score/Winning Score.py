A = []
apple = 0
banana = 0
for i in range(6):
    A.append(int(input()))
    if i < 3:
        if i == 0:
            apple += 3*A[i]
        elif i == 1:
            apple += 2*A[i]
        else:
            apple += A[i]
    else:
        if i == 3:
            banana += 3*A[i]
        elif i == 4:
            banana += 2*A[i]
        else:
            banana += A[i]
if apple > banana:
    print('A')
elif banana > apple:
    print('B')
else:
    print('T')