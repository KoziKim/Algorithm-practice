d, y = map(int, input().split())
dm, ym = map(int, input().split())

a = -d + y
b = -dm + ym

while True:
    if a == b:
        break
    if a > b:
        b = b + ym
    elif b > a:
        a = a + y

print(a)