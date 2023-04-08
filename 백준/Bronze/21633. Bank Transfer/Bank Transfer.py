a = int(input())
b = a*0.01 + 25

if b < 100:
    print(100.00)
elif b > 2000:
    print(2000.00)
else:
    print('%.2f'%(b))