n = int(input())

if n%8 == 1:
    print(1)
elif n%8 == 5:
    print(5)
elif n%4 == 3:
    print(3)
elif n%8 == 4 or n%8 == 6:
    print(4)
else:
    print(2)