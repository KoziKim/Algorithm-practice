t, m, t2, m2 = map(int, input().split())

if t2 > t:
    a = t2*60 + m2 - (t*60 + m)
    print(a, a//30)
elif t2 == t and m2 >= m:
    a = t2*60 + m2 - (t*60 + m)
    print(a, a//30)
else:
    a = (t2+24)*60 + m2 - (t*60 + m)
    print(a, a//30)