a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())

x = [a, c, e, g]
y = [b, d, f, h]

print((max(max(x) - min(x), max(y) - min(y)))**2)