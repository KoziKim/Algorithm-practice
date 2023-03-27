t = input()
a = 0
b = 0
for i in range(len(t)):
    if t[i] == 'A':
        a += 1
    elif t[i] == 'B':
        b += 1
print(a, ':', b)