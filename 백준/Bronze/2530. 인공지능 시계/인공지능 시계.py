h, m, s = map(int, input().split())
time = int(input())

h += (time // 3600)
time %= 3600
s += time % 60
if s >= 60:
    s %= 60
    m += 1
    if m >= 60:
        m %= 60
        h += 1
m += (time // 60)
if m >= 60:
    m %= 60
    h += 1
if h >= 24:
    h %= 24
print(h, m, s)