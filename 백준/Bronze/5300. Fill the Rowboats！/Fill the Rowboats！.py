n = int(input())
i = 1
while n:
    print(i, end = ' ')
    if n == 1 or i % 6 == 0:
        print('Go!', end = ' ')
    i += 1
    n -= 1
