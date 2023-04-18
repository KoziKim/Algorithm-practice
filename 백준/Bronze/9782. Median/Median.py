cnt = 1
while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    if a[0] % 2 == 0:
        ans = (a[int((len(a) + 1)/2)-1] + a[int((len(a) + 1)/2)])/2
    else:
        ans = a[len(a)//2]
    print(f"Case {cnt}: %.1f"%ans)
    cnt += 1