import sys
from itertools import permutations

N = int(sys.stdin.readline())
A = list(map(int, (sys.stdin.readline().split())))
ans = 0

cases = list(permutations(A))

for case in cases:
    tmp = 0
    for i in range(N-1):
        tmp += abs(case[i+1]-case[i])
    ans = max(tmp, ans)

print(ans)