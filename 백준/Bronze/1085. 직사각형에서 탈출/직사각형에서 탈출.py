x, y, w, h = input().split()

x = int(x)
y = int(y)
w = int(w)
h = int(h)

a = min(x, abs(w-x))
b = min(y, abs(h-y))

c = min(a, b)

print(c)