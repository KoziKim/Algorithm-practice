k, n = map(int, input().split())

x = k

if n == 1:
    print(-1)
elif k == 1:
    print(2)
else:
    if n*k % (n-1) != 0:
        print((n*k)//(n-1)+1)
    else:
        print((n*k)//(n-1))