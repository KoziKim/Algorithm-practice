n, h, v = map(int, input().split())

if h*2 >= n and v*2 >= n:
    print(4*h*v)
elif h*2 >= n and v*2 < n:
    print(4*h*(n-v))
elif h*2 < n and v*2 >= n:
    print(4*(n-h)*v)
else:
    print(4*(n-h)*(n-v))