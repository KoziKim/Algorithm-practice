n, w, h, l = map(int, input().split())
if n > (w//l)*(h//l):
    print((w//l)*(h//l))
else:
    print(n)