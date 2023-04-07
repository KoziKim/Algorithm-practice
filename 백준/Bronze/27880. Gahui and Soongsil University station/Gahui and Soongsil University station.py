ans = 0
while True:
    try:
        a = input().split()
        if a[0] == 'Es':
            ans += 21 * int(a[1])
        elif a[0] == 'Stair':
            ans += 17 * int(a[1])
    except:
        print(ans)
        exit()