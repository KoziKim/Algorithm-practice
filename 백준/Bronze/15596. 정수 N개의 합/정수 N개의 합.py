def solve(a):
    ans = 0
    n = len(a)

    for i in range(0, n):
        ans = ans + int(a[i])
    return ans
