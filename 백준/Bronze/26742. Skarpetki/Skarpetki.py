t = input()
b = 0
c = 0
for i in range(len(t)):
    if t[i] == 'B':
        b += 1
    else:
        c += 1
print(b//2 + c//2)