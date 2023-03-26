r = int(input())
c = int(input())

for i in range(r):
    for j in range(c):
        print('*', end = '')
        if j == c - 1:
            print()