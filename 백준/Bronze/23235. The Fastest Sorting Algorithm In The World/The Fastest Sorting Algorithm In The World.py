import sys

inp = sys.stdin.readline
i = 1
while True:
    n = inp()
    if n[0] == '0':
        break
    print("Case %d: Sorting... done!" % i)
    i += 1
