a, b, c, d = map(int, input().split())


num_sqrs = min(a, b) + min(c, d)
i = 0
while True:
    if i**2 <= num_sqrs < (i+1)**2:
        print(i)
        break
    i += 1
