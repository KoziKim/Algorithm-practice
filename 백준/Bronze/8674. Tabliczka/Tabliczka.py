r, c = map(int, input().split())

if r % 2 != 0 and c % 2 != 0:
    print(min(r,c))
else:
    print(0)