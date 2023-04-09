a = int(input())
b = int(input())

if (a+b)%12 == 0:
    print(12)
elif a+b > 12:
    print((a+b)%12)
else:
    print(a+b)