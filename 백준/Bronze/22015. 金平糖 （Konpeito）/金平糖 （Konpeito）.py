a = list(map(int, input().split()))
a.sort()
b = a[2] - a[1]
c = a[2] - a[0]
print(b+c)