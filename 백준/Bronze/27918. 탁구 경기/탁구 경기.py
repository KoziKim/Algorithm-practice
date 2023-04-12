import sys
n = int(input())

d = 0
p = 0
for i in range(n):
    a = sys.stdin.readline().rstrip()
    if a == 'D':
        d += 1
    elif a == 'P':
        p += 1
    if d - p == 2 or p - d == 2:
        print(d, ':', p, sep='')
        break
else:
    print(d, ':', p, sep='')
