Big = int(input())
Small = int(input())
if Big*8 + Small*3 < 28:
    print(0)
else:
    print(Big*8 + Small*3 - 28)