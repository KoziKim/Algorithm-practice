d, h, m = map(int, input().split())

# 11 11 11      11*24*60 + 11*60 + 11

if d < 11:
    print(-1)
elif d == 11 and h < 11:
    print(-1)
elif d == 11 and h == 11 and m < 11:
    print(-1)
else:
    print(d*24*60 + h*60 + m - (11*24*60 + 11*60 + 11))