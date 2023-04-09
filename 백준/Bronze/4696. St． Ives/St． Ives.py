while True:
    a = float(input())
    if a == 0:
        break
    print('%.2f'%(a**4+a**3+a**2+a+1))