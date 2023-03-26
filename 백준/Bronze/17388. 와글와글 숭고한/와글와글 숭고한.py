a, b, c = map(int, input().split())

if a + b + c >= 100:
    print('OK')
else:
    if a < c and a < b:
        print('Soongsil')
    elif b < a and b < c:
        print('Korea')
    elif c < a and c < b:
        print('Hanyang')