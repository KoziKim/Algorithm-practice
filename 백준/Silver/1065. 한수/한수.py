import sys

N = sys.stdin.readline()
M = int(N)
tmp = int()
hnum = 0
a = [0, 0, 0]

for i in range(M+1):
    if i < 100:
        hnum = i
        i += 1
        continue
    else:
        tmp = i
        a[0] = tmp//100
        a[1] = (tmp//10)%10
        a[2] = tmp%10
        if (a[0] - a[1]) == (a[1] - a[2]):
            hnum += 1

print(hnum)