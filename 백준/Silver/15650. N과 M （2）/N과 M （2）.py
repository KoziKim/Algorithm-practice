from itertools import combinations

n, m = map(int, input().split())

if m == 1:
    for i in range(n):
        print(i+1)
else:
    a = [i for i in range(1, n+1)]
    b = list(combinations(a, m))
    b.sort()
    for i in b:
        print(*i)