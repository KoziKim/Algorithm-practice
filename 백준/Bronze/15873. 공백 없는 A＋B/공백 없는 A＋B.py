n = input()
if len(n) == 2:
    a = int(n[0])
    b = int(n[1])
elif len(n) == 3 and n[1] == '0':
    a = int(n[:2])
    b = int(n[-1])
elif len(n) == 3 and n[2] == '0':
    a = int(n[0])
    b = int(n[1:])
else:
    a = 10
    b = 10
print(a+b)