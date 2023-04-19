p, s = map(int, input().split())
s2, p2 = map(int, input().split())

if p+p2 > s+s2:
    print("Persepolis")
elif p+p2 < s+s2:
    print("Esteghlal")
elif p+p2 == s+s2:
    if p2 > s:
        print("Persepolis")
    elif s > p2:
        print("Esteghlal")
    else:
        print("Penalty")
