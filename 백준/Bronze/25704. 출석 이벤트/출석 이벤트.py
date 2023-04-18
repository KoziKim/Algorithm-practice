stamp = int(input())
price = int(input())

c_20 = price * 0.75
c_15 = price - 2000
c_10 = price * 0.9
c_5 = price - 500


if stamp >= 20:
    if price <= 2000:
        print(0)
        exit()
    print(int(min(c_20, c_15)))
elif stamp >= 15:
    if price <= 2000:
        print(0)
        exit()
    print(int(min(c_15, c_10)))
elif stamp >= 10:
    if price <= 500:
        print(0)
        exit()
    print(int(min(c_10, c_5)))
elif stamp >= 5:
    if price <= 500:
        print(0)
    else:
        print(price - 500)
else:
    print(price)