t = int(input())
f = 0
for i in range(t):
    a = list(map(int, input().split()))
    n = a[0]
    ans = a[1:]
    print("Denominations:", *ans)
    for j in range(1, n+1):
        if j == n:
            continue
        if 2 * a[j] > a[j+1]:
            f = 1
    if f == 1:
        print("Bad coin denominations!\n")
    else:
        print("Good coin denominations!\n")
    f = 0